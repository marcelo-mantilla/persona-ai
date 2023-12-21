from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from src.avatar.models import *
from src.post.models import Post
from src.services.action_service import ActionService
from src.services.image_service import ImageService

def create_post(request):
    avatar_id = ""
    avatar = get_object_or_404(Avatar, id=avatar_id)

    action_service = ActionService(avatar)
    action = action_service.brainstorm_action()
    caption = action_service.brainstorm_caption(action)

    image_service = ImageService(avatar, action, caption)
    image_url = image_service.generate_image()

    post = Post(
        avatar=avatar,
        image_url=image_url,
        caption=caption
    )






    return HttpResponse("Hello, world. You're at the post index.")
