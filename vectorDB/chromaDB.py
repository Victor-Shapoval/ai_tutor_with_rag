from google import genai
from google.genai import types
# Для автоматической повторной попытки в случае ошибок API
from google.api_core import retry
# Для обработки текста и деления на чанки
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from chromadb import Documents, EmbeddingFunction, Embeddings, PersistentClient
from pathlib import Path
import shutil


# определение рабочих каталогов
# Переходим в корень проекта (../)
BASE_DIR = Path(__file__).resolve().parent.parent
MD_DIR = './MD_files'


#  ===  ===  ===  ===  ===  === Вспомогательные функциии и классы === === === === === ===


def is_retriable(e):
    """
    Проверяет, является ли ошибка API-системы Google GenAI временной, и если да, то позволяет повторить запрос.
    :param e: Исключение (ошибка), которое было поднято в процессе выполнения запроса.
    :type e: Exception
    :return: Возвращает True, если ошибка является временной (код 429 или 503), иначе False.
    :rtype: bool
    """
    return (isinstance(
        e, genai.errors.APIError) and e.code in {429, 503})

# --- Вспомогательная функция для разделения списка на батчи ---


def batch_list(data, batch_size: int):
    """Делит список на более мелкие списки (батчи) заданного размера."""
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# Class GeminiEmbeddingFunction наследует EmbeddingFunction и реализует метод __call__


class GeminiEmbeddingFunction(EmbeddingFunction):
    def __init__(self, client, document_mode=True):
        """
        Конструктор класса GeminiEmbeddingFunction.
        :param client: Объект клиента GenAi для выполнения вызовов API.
        """
        self.client = client
        self.document_mode = document_mode

    # Декоратор для автоматической повторной попытки в случае ошибок API
    @retry.Retry(predicate=is_retriable)
    def __call__(self, input: Documents) -> Embeddings:
        """
        Метод для получения эмбендингов (embeddings) для документов или запросов.
        :param input: Документы, для которых нужно извлечь эмбендинги.
        document_mode: Этот флаг указывает, что класс будет работать с документами, а не с запросами
        :return: Список эмбендингов для данных документов.
        """
        # Определяем, какой тип эмбендинга будет использоваться (для документа или запроса)
        if self.document_mode:
            embedding_task = "retrieval_document"  # Тип задания: обработка документов
        else:
            embedding_task = "retrieval_query"  # Тип задания: обработка запросов

        # Вызов API Google GenAI для извлечения эмбендингов
        response = self.client.models.embed_content(
            model="models/text-embedding-004",  # Используемая модель для эмбендинга текста
            contents=input,  # Содержимое документов для эмбендингов
            config=types.EmbedContentConfig(
                task_type=embedding_task,  # Тип задачи (документ или запрос)
            ),
        )

        # Возвращаем эмбендинги как список значений
        return [e.values for e in response.embeddings]


def _split_file_to_chunks(file_path: str, text_splitter) -> list[str]:
    """Считывает файл и разбивает его содержимое на чанки."""
    with open(file_path, 'r', encoding='utf-8') as file:
        document = file.read()
    return text_splitter.split_text(document)


def load_md_files_and_split(folder_path, add_file=False, chunk_size=1000, chunk_overlap=100):
    """
    Загружает все MD файлы из папки и делит их на чанки с использованием RecursiveCharacterTextSplitter
    :param folder_path: Путь к папке с MD файлами
    :param max_chunk_size: Максимальный размер чанка (по символам)
    :return: Список документов (чанков)
    """
    documents = []

    # Инициализация TextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    if add_file:
        file_path = folder_path
        filename = os.path.basename(file_path)
        chunks = _split_file_to_chunks(file_path, text_splitter)
        for chunk in chunks:
            documents.append({"text": chunk, "source": os.path.splitext(filename)[0]})
    else:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            chunks = _split_file_to_chunks(file_path, text_splitter)
            for chunk in chunks:
                documents.append({"text": chunk, "source": os.path.splitext(filename)[0]})
    return documents


# ===  ===  ===  ===  ===  === Основной класс === === === === === ===

class ChromaDBManager:
    def __init__(self, db_name, persist_dir, api_key):
        """
        Инициализация менеджера базы данных Chroma и автоматическая загрузка/создание базы данных.
        :param db_name: Имя базы данных.
        :param persist_dir: Путь для сохранения базы данных.
        :param api_key: API ключ для Google GenAI.
        """
        self.db_name = db_name
        self.persist_dir = persist_dir
        self.api_key = api_key
        self.client = genai.Client(api_key=self.api_key)
        self.db_path = os.path.join(self.persist_dir, "chroma_data")
        # счетчик id необходимо вести что бы не перезаписывать старые файлы на новые
        self.id_count = None

        # Используем PersistentClient для работы с локальным хранилищем
        self.chroma_client = PersistentClient(path=self.db_path)

        self.embed_fn = GeminiEmbeddingFunction(self.client)

        # Создает или загружает базу данных из папки
        self.db = self.create_or_load_db()

    def create_or_load_db(self, rebase=False):
        """
        Создает или загружает базу данных. Если база данных пуста, загружает файлы и добавляет их.
        :params: rebase=True производит очистку текущей БД перед инициализацей новой
        :return: Инициализированная база данных.
        """
        if rebase:
            try:
                self.chroma_client.delete_collection(name=self.db_name)
            except ValueError:
                # Игнорируем ошибку, если коллекция не существует
                print(
                    f"Коллекция '{self.db_name}' не найдена или уже удалена. Продолжаем.")

        db = self.chroma_client.get_or_create_collection(
            name=self.db_name, embedding_function=self.embed_fn
        )

        self.id_count = db.count()

        if db.count() == 0:
            # Если база пустая загружаем и делим на чанки файлы из папки
            documents = load_md_files_and_split(
                MD_DIR, chunk_size=1000)

            # Делим наш большой список на список списков по 100 элементов
            batch_doc = batch_list(documents, 99)
            # И добавляем в нашу базу
            for batch in batch_doc:
                db.add(
                    documents=[doc["text"] for doc in batch],
                    metadatas=[{"source": doc["source"]} for doc in batch],
                    ids=[f"id_{self.id_count + i}" for i in range(len(batch))])
                # обновим счетчик что бы исключить перезапись в базе
                self.id_count += len(batch)

        return db

    def search_in_database(self, query: str, top_n: int = 3):
        """
        Ищет в базе данных Chroma по заданному запросу.
        :param query: Запрос для поиска.
        :param top_n: Количество результатов, которое нужно вернуть.
        :return: Результаты поиска в виде списка top_n чанков
        """
        self.embed_fn.document_mode = False
        result = self.db.query(query_texts=[query], n_results=top_n)
        docs = result["documents"][0]
        metas = result["metadatas"][0]
        return list(zip(docs, metas))

    def add_documents(self, document, chunk_size=1000):
        """
        Добавляет документы в базу данных Chroma.
        :param documents: Список документов для добавления.
        :param chunk_size: Размер чанков для разбиения документов.
        """
        documents = load_md_files_and_split(
            document, add_file=True, chunk_size=chunk_size)
        # разбиваем по 100 элементов
        batch_doc = batch_list(documents, 99)
        # И добавляем в нашу базу
        for batch in batch_doc:
            for batch in batch_doc:
                self.db.add(
                    documents=[doc["text"] for doc in batch],
                    metadatas=[{"source": doc["source"]} for doc in batch],
                    ids=[f"id_{self.id_count + i}" for i in range(len(batch))])
            self.id_count += len(batch)
