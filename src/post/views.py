from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse

from src.post.models import *
from src.services.action_service import ActionService
from src.services.image_service import ImageService
from src.services.twitter import Twitter

@csrf_exempt
def create_post(request):
    try:
        avatar_id = "1"
        avatar = get_object_or_404(Avatar, id=avatar_id)

        action_service = ActionService(avatar)
        action = action_service.brainstorm_action()
        caption = action_service.brainstorm_caption(action)

        image_service = ImageService(avatar, action, caption)
        image_url, image_desc = image_service.generate_image()

        print("Image URL:", image_url)
        print("Action:", action)
        print("Caption:", caption)

        post = Post(
            avatar=avatar,
            action=action,
            caption=caption,
            description=image_desc,
        )
        post.save()

        twitter = Twitter()
        media_data = twitter.create_media(image_url)

        media = Media(
            post=post,
            image_url=image_url,
            image_description=image_desc,
            twitter_media_id=media_data.media_id_string,
            twitter_media_key=media_data.media_key,
            twitter_height=media_data.image['h'],
            twitter_width=media_data.image['w'],
        )
        media.save()

        twitter.create_post_with_media(post)
        return HttpResponse("Post created successfully.")

    except Exception as e:
        print("Internal Server Error:", e)


def create_hottake(request):
    try:
        avatar_id = "1"
        avatar = get_object_or_404(Avatar, id=avatar_id)

        action_service = ActionService(avatar)
        status = action_service.brainstorm_status()

        print('status:', status)

        post = Post(
            avatar=avatar,
            caption=status,
        )
        post.save()

        twitter = Twitter()
        twitter.create_status_post(post)

    except Exception as e:
        print("Internal Server Error:", e)

def trending_posts_tweets(request):
    try:
        twitter = Twitter()
        twitter.get_trending_tweets()
    except Exception as e:
        print("Internal Server Error:", e)

    return HttpResponse("Hello, world. You're at the post index.")