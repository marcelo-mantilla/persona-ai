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
        try:
            image_data = None
            response = requests.get(image_url)

            if response.status_code == 200:
                image_data = response.content
            else:
                Exception(f"Could not retrieve image via URL: {image_url}")

            print('uploading media image...')
            media_data = self.v1_client.simple_upload(
                filename='generated-dalle3-image',
                file=image_data,
                media_category='tweet_image'
            )
        except Exception as e:
            print(f"Error creating media: {e}")
            raise e

        return media_data

    def create_post_with_media(self, post: Post):
        try:
            media_ids = post.media.all().values_list('twitter_media_id', flat=True)

            print('media_ids', media_ids)

            self.v2_client.create_tweet(
                media_ids=media_ids,
                text=post.caption,
            )
        except Exception as e:
            print(f"Error creating post with media: {e}")
            raise e

    def create_status_post(self, post: Post):
        try:
            self.v2_client.create_tweet(
                text=post.caption,
            )
        except Exception as e:
            print(f"Error creating status post: {e}")
            raise e

