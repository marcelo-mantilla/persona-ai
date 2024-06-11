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

    avatar = get_object_or_404(Avatar, id=avatar_id)
    orchestrator = Orchestrator(avatar=avatar)
    hot_take: str = orchestrator.hot_take(instruction)

    print("Hot take output: ", hot_take)

    return Response(
        status=status.HTTP_200_OK,
        data={
            "hot_take": hot_take,
        }
    )

@api_view(['POST'])
def create_post(request):
    pass