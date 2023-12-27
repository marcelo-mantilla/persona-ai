import requests
import tweepy
import os

from src.post.models import *

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuth1UserHandler(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET'),
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
        )
        self.v1_client = tweepy.API(auth=self.auth, retry_count=2)
        self.v2_client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
        )
        pass

    def create_media(self, image_url):
        image_data = None
        response = requests.get(image_url)

        if response.status_code == 200:
            image_data = response.content
        else:
            Exception(f"Could not retrieve image via URL: {image_url}")

        media_data = self.v1_client.simple_upload(
            filename='generated-dalle3-image',
            file=image_data,
            media_category='twitter_image'
        )

        return media_data

    def create_post_with_media(self, post: Post):
        media_ids = post.media.all().values_list('twitter_media_key', flat=True)

        self.v2_client.create_tweet(
            media_ids=media_ids,
            text=post.caption,
        )

    def create_status_post(self, post: Post):
        self.v2_client.create_tweet(
            text=post.caption,
        )
