from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from src.avatar.models import *
from src.post.models import Post
from src.services.action_service import ActionService
from src.services.image_service import ImageService

def create_post(request):
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
        image_url=image_url,
        image_description=image_desc,
    )
    post.save()



    return HttpResponse("Hello, world. You're at the post index.")

