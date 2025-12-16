import os
from pathlib import Path, PosixPath
from docling.document_converter import DocumentConverter
import logging

# инициализация логера
logger = logging.getLogger(__name__)

# определение рабочих каталогов
BASE_DIR = Path(__file__).resolve().parent.parent # Переходим в корень проекта (../)
PDF_DIR = BASE_DIR / 'PDF_files'
MD_DIR = BASE_DIR / 'MD_files'

# ===  ===  ===  ===  ===  === Вспопогательные функциии === === === === === ===

def __converter_initializer__() -> DocumentConverter:
    """Инициализатор конвертера
    Возвращает инициализированный конвертер"""
    try:
        converter = DocumentConverter()
        logger.info("Конвертер инициализирован")
        return converter
    except Exception as e:
        logger.error("Ошибка инициализации конвертера")
        return

def __parse_pdf_to_markdown__(converter: DocumentConverter,
                        pdf_path: PosixPath, 
                        md_path: PosixPath) -> PosixPath:
    """Парсер файла формата .pdf в формат .md.

    Берет один файл pdf по указанному пути из PDF_DIR, парсит их с помощью Docling,
    сохраняет результат в Markdown в каталог MD_DIR и возвращает путь до сохраненного файла.

    Принимает:
    convert: DocumentConverter - инициализированный конвертер
    pdf_path: pathlib - путь до файла .pdf
    md_path: pathlib  - путь до каталога с файлами .md
    
    Возвращает:
    pathlib.PosixPath - путь до конвертированного файла .md

    Примечание:
    НЕ проверяет на наличие каталога md_path
    """

    # формируем путь для выходного файла .md
    md_filename = pdf_path.stem + ".md"
    md_path = md_path / md_filename

    # проверяем на наличие конвертированного файла в папке, если существует то выходим
    if md_path.exists():
        logger.info(f"Файл существует: {md_path.name}")
        return md_path

    try:
        # конвертация документа
        result = converter.convert(str(pdf_path))

        # извлечение содержимого в Markdown
        markdown_content = result.document.export_to_markdown()

        # сохраняем Markdown в файл
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        logger.info(f"Успешно сохранено: {md_path.name}")
        return md_path

    except Exception as e:
        logger.error(f"Ошибка при обработке {pdf_path.name}: {e}")
        return

# ===  ===  ===  ===  ===  === Публичные доступные функциии === === === === === ===

def one_pdf_to_markdown(pdf_path: PosixPath) -> PosixPath:
    """Обработка одного PDF-файла из PDF_DIR и сохранением результата в Markdown в MD_DIR
    Принимает:
    pdf_path: pathlib - путь до файла .pdf
    
    Возвращает:
    pathlib.PosixPath - путь до конвертированного файла .md """

    # проверяем и создаем целевой каталог
    MD_DIR.mkdir(parents=True, exist_ok=True)
    
    # инициализация конвертера Docling
    converter = __converter_initializer__()

    # парсин файла pdf
    md_path = __parse_pdf_to_markdown__(converter=converter, pdf_path=pdf_path, md_path=MD_DIR)

    return md_path


def all_pdfs_to_markdown():
    """Обработка всех PDF-файлов из PDF_DIR и сохранением результатов в Markdown в MD_DIR"""

    # проверяем и создаем целевой каталог
    MD_DIR.mkdir(parents=True, exist_ok=True)
    
    # инициализация конвертера Docling
    converter = __converter_initializer__()

    # итерирование по всем PDF-файлам - используем glob() для поиска всех файлов с расширением .pdf
    logger.info(f"Начало обработки всех файлов PDF")

    for pdf_path in PDF_DIR.glob("*.pdf"):
        # вызываем функцию парсинга, путь до файла в /dev/null
        _ = __parse_pdf_to_markdown__(converter=converter, pdf_path=pdf_path, md_path=MD_DIR)
    
    logger.info("Конвертация всех файлов завершена")
    
    return

## тест
# md_path = one_pdf_to_markdown(PDF_DIR/'Документ_1')
# print()
# print(md_path)
# print(type(md_path))

# all_pdfs_to_markdown()
