import os
import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import vectorDB.chromaDB as dbm
from dotenv import load_dotenv
from aiogram.types import Message, FSInputFile, ContentType
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramNetworkError
import document_parser.dockling_doc as docling
import llm_api.Google_Gemini as Google_Gemini


# Настройка системного логирования
# Директория для логов
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
log_file = LOG_DIR / "system_log.txt"
# Создание логера
logger = logging.getLogger("telegram_bot")
logger.setLevel(logging.INFO)
# Разделение логов на файлы
file_handler = RotatingFileHandler(filename=str(log_file), mode="a",
                                   maxBytes=10 * 1024 * 1024, backupCount=30, encoding="utf-8",)
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S",)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Загрузка переменных из .env
load_dotenv()

# Определение рабочих каталогов
BASE_DIR = Path(__file__).resolve().parent  # Переходим в корень проекта (../)
PDF_DIR = BASE_DIR / 'PDF_files'
MD_DIR = BASE_DIR / 'MD_files'

# Загрузка данных из переменных окружения
# - Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    logger.error("Не задана переменная окружения TELEGRAM_BOT_TOKEN")
    raise ValueError("Не задан TELEGRAM_BOT_TOKEN в .env")
else:
    logger.info("TELEGRAM_BOT_TOKEN загружен успешно")

# - Google
GOOGLE_API = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API:
    logger.error("Не задана переменная окружения GOOGLE_API_KEY")
    raise ValueError("Не задан GOOGLE_API_KEY в .env")
else:
    logger.info("GOOGLE_API_KEY загружен успешно")

# - Администраторы бота
ADMIN_IDS = os.getenv("ADMIN_IDS", "")
ADMIN_IDS_LIST = [int(x.strip()) for x in ADMIN_IDS.split(",") if x.strip()]
# - Имя базы данных / Директория
DB_NAME = os.getenv("DB_NAME")
PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY")

# Состояние для хранения информации о том от кого ожидаем PDF
waiting_for_pdf = set()

# Инициализация бота и диспетчера
telegram_bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Инициализация базы данных
try:
    db_manager = dbm.ChromaDBManager(
        db_name=DB_NAME, persist_dir=PERSIST_DIRECTORY, api_key=GOOGLE_API)
    logger.info("DB manager успешно инициализирован (при старте)")
except Exception as e:
    db_manager = None
    logger.exception(
        "Ошибка при первоначальной инициализации ChromaDBManager: %s", e)

# Считываем иснтрукции для модели
try:
    with open("instruction_material_tutor.txt", "r", encoding="utf-8") as f:
        instruction_material_tutor = f.read()
    with open("instruction_question_tutor.txt", "r", encoding="utf-8") as f:
        instruction_question_tutor = f.read()

    logger.info("Системная инструкция загружена.")
except Exception as e:
    system_instruction = ""
    logger.exception("Не удалось загрузить instruction_material_tutor.txt: %s", e)

# Инициализация клиента для модели
try:
    GeminiAgent = Google_Gemini.GeminiAgent(model = "gemini-2.5-flash", name = "agents",
                                            instruction=instruction_material_tutor, api_key = GOOGLE_API)
    logger.info("Google genai Agent material_tutor инициализирован")
except Exception as e:
    client = None
    logger.exception("Ошибка инициализации Gemini Agent material_tutor: %s", e)


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    photo = FSInputFile("./_addons/ded.jpeg")
    welcome_text = (
        "👴 Ох-хо-хо! Здравствуй, внучек!\n"
        "Я — Джоуль Петрович, старый, но ещё искрящийся дед 🤓⚡\n\n"
        "🔌 В моё время лампочки не мигали, потому что мы им не позволяли!\n"
        "Так что если у тебя есть вопросы по энергетике — не стесняйся, подходи ближе\n\n"
        "💡 Объясню, что крутится, где греется и почему не стоит тыкать пальцем в розетку\n\n"
    )
    await message.answer_photo(photo=photo, caption=welcome_text)

# Обработчик команды /self_check_on
@dp.message(Command("self_check_on"))
async def cmd_update_db(message: Message):
    user_id = message.from_user.id
    global GeminiAgent
    # Изменяем инструкцию агента
    try:
        GeminiAgent.set_instruction(instruction_question_tutor)
        logger.info("Google genai Agent question_tutor инициализирован")
    except Exception as e:
        logger.exception("Ошибка инициализации Gemini Agent question_tutor: %s", e)
    prompt = "Я хочу начать отвечать на вопросы - спроси у меня тему"
    response = await GeminiAgent.run_session(user_queries=prompt, session_id=user_id,
                                             app_name="agents", user_id=user_id)
    # Отправка ответа пользователю
    await message.reply(response)

# Обработчик команды /self_check_off
@dp.message(Command("self_check_off"))
async def cmd_update_db(message: Message):
    user_id = message.from_user.id
    global GeminiAgent
    # Изменяем инструкцию агента
    try:
        GeminiAgent.set_instruction(instruction_material_tutor)
        logger.info("Google genai Agent material_tutor инициализирован")
    except Exception as e:
        logger.exception("Ошибка инициализации Gemini Agent material_tutor: %s", e)
    prompt = "Я перестаю отвечать на вопросы, вернусь к изучению материалов с твоей помощью"
    response = await GeminiAgent.run_session(user_queries=prompt, session_id=user_id,
                                             app_name="agents", user_id=user_id)
    # Отправка ответа пользователю
    await message.reply(response)


# Обработчик команды /update_db
@dp.message(Command("update_db"))
async def cmd_update_db(message: Message):
    user_id = message.from_user.id
    logger.info("Запрошена инициализация базы пользователем %s", user_id)
    if user_id not in ADMIN_IDS_LIST:
        logger.warning(
            "Пользователь %s пытался вызвать обновление базы без прав", user_id)
        await message.reply("❌ У вас нет прав на обновление базы базы!")
        return

    # Проверяем и создаем целевой каталог, если его нет
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    # Парсинг всех pdf файлов
    await message.reply("Началась инициализация базы данных...!\n\nПроцесс может занять некоторое время")
    docling.all_pdfs_to_markdown()

    # Сброс базы и добавление всех файлов
    db_manager.create_or_load_db(rebase=True)
    await message.reply("✅ База инициализирована, все документы добавлены!")


# Обработчик команды /download_pdf
@dp.message(Command("download_pdf"))
async def cmd_update_db(message: Message):
    user_id = message.from_user.id
    logger.info("Запрошено загрузка PDF пользователем %s", user_id)
    if user_id not in ADMIN_IDS_LIST:
        logger.warning(
            "Пользователь %s пытался вызвать загрузку PDF без прав", user_id)
        await message.reply("❌ У вас нет прав на дополнение базы!")
        return
    waiting_for_pdf.add(user_id)
    await message.reply("📄 Пожалуйста, пришлите PDF-файл для дополнения векторной базы")


# Обработчик Запросов
@dp.message(F.text)
async def handle_text(message: Message):
    user_id = message.from_user.id
    user_query = message.text
    logger.info("Запрос от user_id=%s: %s", user_id, user_query)

    # Поиск в базе
    try:
        top_results = db_manager.search_in_database(user_query, top_n=3)

        # Формируем промпт
        prompt = "Используя следующие материалы:\n"
        for text, meta in top_results:
            prompt += f"[Источник: {meta['source']}]\n{text}\n\n"
        prompt += f"\nОтветь на вопрос пользователя:\n{user_query}"

        # Запрос к модели
        response = await GeminiAgent.run_session(user_queries = prompt, session_id = user_id,
                                                 app_name="agents", user_id = user_id)


        # Отправка ответа пользователю
        await message.reply(response)
    except Exception as e:
        logger.exception(
            "Ошибка при обработке текстового запроса user_id=%s: %s", user_id, e)
        await message.reply("❌ Произошла ошибка при обработке запроса.")

# Обработчик PDF-файлов
@dp.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def handle_pdf(message: Message):
    user_id = message.from_user.id
    logger.info("Получен документ от user_id %s", user_id)
    # Проверяем, ждем ли от этого пользователя PDF
    if user_id not in waiting_for_pdf:
        logger.debug(
            "Не ожидался PDF от user_id %s — не обрабатываем!", user_id)
        return

    # Проверяем, что файл PDF
    if not message.document.file_name.lower().endswith(".pdf"):
        logger.warning("Пользователь %s прислал не PDF-файл", user_id)
        await message.reply("❌ Это не PDF-файл. Попробуйте ещё раз")
        return

    await message.reply(f"✅ Получен PDF: {message.document.file_name}. Добавление документа...")

    # Проверяем и создаем целевой каталог
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    # Сохранение файла
    file_name = message.document.file_name
    file_id = message.document.file_id
    save_path = PDF_DIR / file_name
    await message.bot.download(file=file_id, destination=save_path)
    logger.info("PDF-файл %s сохранен в %s", file_name, save_path)

    # Вызов функции парсинга pdf
    md_path = docling.one_pdf_to_markdown(pdf_path=save_path)

    # Добавляем файл в базу
    db_manager.add_documents(md_path)
    await message.reply("✅ Документ добавлен. База обновлена!")

    # Снимаем флаг ожидания
    waiting_for_pdf.remove(user_id)


# запуск бота
async def main():
    try:
        # Проверка подключения
        _ = await telegram_bot.get_me()
        # Запуск polling
        logger.info("Запуск polling...")
        await dp.start_polling(telegram_bot)
    except TelegramNetworkError as e:
        logger.exception("Ошибка сети при работе бота: %s", e)
    except Exception as e:
        logger.exception("Неожиданная ошибка в main: %s", e)
    finally:
        logger.info("Бот остановлен")
        await telegram_bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
