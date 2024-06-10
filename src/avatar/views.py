from django.shortcuts import render
from rest_framework.decorators import api_view

from src.avatar.serializers import HotTakeSerializer


@api_view(['POST'])
def create_hot_take(request):
    serializer = HotTakeSerializer(data=request.data)
    pass

@api_view(['POST'])
def create_post(request):
    pass