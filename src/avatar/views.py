from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from src.avatar.models import Avatar
from src.avatar.serializers import HotTakeSerializer
from src.services.action_service import ActionService


@api_view(['POST'])
def create_hot_take(request, avatar_id):
    HotTakeSerializer(data=request.data)

    avatar = get_object_or_404(Avatar, id=avatar_id)

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