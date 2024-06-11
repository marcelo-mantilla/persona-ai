import os
import requests
import instructor
from openai import OpenAI

from src.instructor.models import NewsData
from src.services.prompt_manager import PromptManager
from src.services.service import Service

NEWSDATA_URL = "https://newsdata.io/api/1"
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

class NewsService(Service):
    def __init__(self):
        self.openai_client = instructor.from_openai(OpenAI())
        self.prompt_manager = PromptManager()

    def summarize_news(
        self,
        keywords: list[str],
        individuals: list[str],
        countries: list[str]
    ) -> NewsData:
        try:
            news_data = self._newsdata_request(keywords, countries, individuals)
            news_data.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error fetching news data: ", e)
            raise e

        data = news_data.json()
        index = data.get('results', [])
        if not index:
            raise ValueError("No news found.")

        news_as_string = ""
        for news in index:
            news_as_string += self.prompt_manager.format_news_as_string(
                title=news.get('title', ''),
                source_url=news.get('source_url', ''),
                category=news.get('category', ''),
                description=news.get('description', ''),
            )

        print("News as string: ", news_as_string)

        system_prompt = self.prompt_manager.news_description_summary_prompt()
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": news_as_string},
        ]
        return self.openai_client.chat.completions.create(
            model="gpt-4o",
            response_model=NewsData,
            messages=messages,
            temperature=0.8,
        )

    ### PRIVATE ###

    def _newsdata_request(
        self,
        keywords: list[str],
        countries: list[str],
        individuals: list[str],
    ):
        params = {
            "size": 10,
            "prioritydomain": "top",
            "q": self._compose_newsdata_search_query(keywords, individuals),
            **({"country": self._compose_newsdata_countries_query(countries)} if countries else {})
        }

        return requests.get(
            url=f"{NEWSDATA_URL}/latest",
            params=params,
            headers={
                "X-Access-Key": f"{NEWSDATA_API_KEY}"
            }
        )

    @staticmethod
    def _compose_newsdata_search_query(
            keywords: list[str],
            individuals: list[str],
    ) -> str:
        keywords = " OR ".join(keywords) if keywords else ""
        individuals = " OR ".join(individuals) if individuals else ""

        if not individuals:
            return keywords

        return f"({keywords}) AND ({individuals})"

    @staticmethod
    def _compose_newsdata_countries_query(countries: list[str]) -> str:
        countries = countries[:5]
        return ",".join(countries) if countries else ""


