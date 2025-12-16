import os
import asyncio
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import preload_memory
from google.adk.runners import Runner
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService

# ===  ===  ===  ===  ===  === Класс агента === === === === === ===

class GeminiAgent:
    def __init__(self, model, name, instruction, api_key):
        self.model = model
        self.name = name
        self.instruction = instruction
        self.key = api_key

        # Общие сервисы для сессий и памяти
        self.session_service = InMemorySessionService()
        self.memory_service = InMemoryMemoryService()

        # Создание агента и Runner
        self.agent = self._create_agent()
        self.runner = self._create_runner()

    def _create_agent(self):
        """
        Создание агента с конфигурацией при ошибках
        """

        # Подбрасываем ключ в переменные окружения
        os.environ["GOOGLE_API_KEY"] = self.key

        # Конфигурация
        retry_config = types.HttpRetryOptions(
            attempts=5,
            exp_base=7,
            initial_delay=1,
            http_status_codes=[429, 500, 503, 504],
        )
        # Создаем LlmAgent с моделью Gemini, инструкцией и инструментами
        agent = LlmAgent(
            model=Gemini(model=self.model, retry_options=retry_config),
            name=self.name,
            instruction=self.instruction,
            tools=[preload_memory],
        )
        return agent

    def _create_runner(self):
        """
        Создание runner для связи агента с сессиями и памятью
        """

        runner = Runner(
            agent=self.agent,
            app_name=self.name,
            session_service=self.session_service,
            memory_service=self.memory_service,
        )
        return runner

    def set_instruction(self, instruction):
        """
        Пересоздаёт агента и runner с инструкцией,
        но сохраняет сессии и память.
        """
        self.instruction = instruction
        self.agent = self._create_agent()
        self.runner = self._create_runner()

    async def run_session(self, user_queries, session_id, app_name, user_id):
        """
        Создает сессию (или получает существующую) и запускает запрос к модели.
        Возвращает текст ответа модели.
        """

        # Приводим идентификаторы к строкам
        user_id = str(user_id)
        session_id = str(session_id)

        # Создаем или получаем сессию
        try:
            session = await self.session_service.create_session(
                app_name=app_name,
                user_id=user_id,
                session_id=session_id,
            )
        except Exception:
            session = await self.session_service.get_session(
                app_name=app_name,
                user_id=user_id,
                session_id=session_id,
            )

        # Небольшая пауза, чтобы сессия точно зарегистрировалась в памяти Runner
        await asyncio.sleep(0.5)

        # Подготовка запроса
        query_content = types.Content(role="user", parts=[types.Part(text=user_queries)])

        # Асинхронно получаем ответ от модели
        async for event in self.runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=query_content,
        ):
            if event.is_final_response() and event.content and event.content.parts:
                text = event.content.parts[0].text
                if text and text != "None":
                    return text

        # Если ответ пустой
        return ""
