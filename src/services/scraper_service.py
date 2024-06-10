import requests
from pydantic import BaseModel
from bs4 import BeautifulSoup as bs
from openai import OpenAI
import instructor

from src.services.service import Service

class NewsData(BaseModel):
    title: str
    detailed_summary: str

class ScraperService(Service):
    def __init__(self):
        self.client = instructor.from_openai(OpenAI())
        pass

    def scrape_website(self, url: str) -> NewsData:
        response = requests.get(url)
        content_type = response.headers['content-type']
        content = None

        if 'application/json' in content_type:
            content = response.json()
        elif 'text/html' in content_type:
            soup = bs(response.content, 'html.parser')
            content = soup.prettify()
        else:
            content = response.text

        print("NEWS DATA:", content)

        # gpt-3.5-turbo-1106 summary


        return 'news!'

