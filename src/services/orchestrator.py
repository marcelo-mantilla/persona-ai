from src.avatar.models import Avatar
from pydantic import BaseModel
from openai import OpenAI
import instructor
import requests

from src.instructor.models import Instruction, NewsData, Status
from src.services.date_service import DateService
from src.services.prompt_manager import PromptManager
from src.services.news_service import NewsService


class Orchestrator:
    def __init__(self, avatar=Avatar):
        self.avatar = avatar
        self.openai_client = instructor.from_openai(OpenAI())
        self.prompt_manager = PromptManager()
        self.news_service = NewsService()
        self.date_service = DateService()

    def generic_hot_take(self, search: bool) -> str:
        pass

    def brainstorm_action(self, instruction: str):
        """
        The brainstorm action method selects what type of action the avatar should take, based on certain
        parameters like date and time, career, hobbies, news, etc.
        """
        pass

    def hot_take(self, instruction) -> str:
        system_prompt = self.prompt_manager.instruction_data_extraction_prompt()
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": instruction},
        ]

        instruction = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_model=Instruction,
            messages=messages
        )

        if not instruction.is_valid():
            raise ValueError("Invalid instruction request.")

        news_summary_data: NewsData = self.news_service.summarize_news(
            individuals=instruction.mentioned_individuals,
            countries=instruction.relevant_countries,
            keywords=instruction.keywords,
        )

        print("News summary data: ", news_summary_data.json())

        messages = [
            {"role": "user", "content": self.avatar.persona_template.as_prompt()},
            {"role": "user", "content": news_summary_data.summary},
            {"role": "user", "content": instruction.instruction},
            {"role": "system", "content": self.prompt_manager.hot_take_prompt()},
        ]

        hot_take = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            response_model=Status,
            max_tokens=400,
            temperature=0.8,
        )

        print("Hot take output: ", hot_take.status)

        return hot_take.status
