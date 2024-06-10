from src.avatar.models import Avatar
from pydantic import BaseModel
from openai import OpenAI
import instructor
import requests

from src.services.prompt_manager import PromptManager
from src.services.scraper_service import ScraperService, NewsData


class Orchestrator:
    def __init__(self, avatar=Avatar):
        self.avatar = avatar
        self.openai_client = instructor.from_openai(OpenAI())
        self.prompt_manager = PromptManager()
        self.scraper = ScraperService()

    def hot_take(self, instruction: str, news_url: str) -> str:
        system_prompt = self.prompt_manager.hot_take_data_extraction_prompt()
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": instruction},
        ]

        hot_take_data: HotTake = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_model=HotTake,
            messages=[{"role": "user", "content": instruction}]
        )

        if not hot_take_data.is_valid():
            raise ValueError("Invalid hot take request.")

        if hot_take_data.news_url:
            print('News url: ', hot_take_data.news_url)
            news_data: NewsData = self.scraper.scrape_website(hot_take_data.news_url)
            pass
            # news_data = client.chat.completions.create(
            #     model="gpt-4o",
            #     response_model=NewsData,
            #     messages=[{"role": "system", "content": "Fetch news data from the provided URL."}],
            # )
            # print("News data: ", news_data.json())

        return "hot take here"


class HotTake(BaseModel):
    instruction: str
    news_url: str
    mentioned_individuals: list[str]
    intention: str

    def is_valid(self):
        if not self.instruction and not self.intention:
            return False
        return True

