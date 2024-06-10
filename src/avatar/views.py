from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from src.avatar.models import Avatar
from src.avatar.serializers import HotTakeSerializer
from src.post.models import Post
from src.services.action_service import ActionService
from src.services.orchestrator import Orchestrator


@api_view(['POST'])
def create_hot_take(request, avatar_id):
    serializer = HotTakeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    instruction: str = serializer.data.get('instruction', None)
    news_url: str = serializer.data.get('news_article_url', None)

    avatar = get_object_or_404(Avatar, id=avatar_id)

    orchestrator = Orchestrator(avatar=avatar)
    hot_take: str = orchestrator.hot_take(instruction, news_url)

    print("Hot take output: ", hot_take)

    return Response(
        status=status.HTTP_200_OK,
        data={
            "hot_take": hot_take,
        }
    )

    post = Post(
        avatar=avatar,
        caption=hot_take,
    )
    post.save()



    action_service = ActionService(avatar)
    generated_status: str = action_service.brainstorm_status()

    print("Status:", generated_status)

    return Response(
        status=status.HTTP_200_OK,
        data={
            "status": generated_status,
        }
    )

@api_view(['POST'])
def create_post(request):
    pass