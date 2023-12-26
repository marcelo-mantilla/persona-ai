import tweepy
import uuid
import os

class Twitter:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
        )
        pass

    def create_life_post(self, image_url: str):
        media_key = uuid.uuid4()
        type = "photo"
        url = image_url
        height = "1792"
        width = "1024"
        alt_text = "to be put here"

        pass