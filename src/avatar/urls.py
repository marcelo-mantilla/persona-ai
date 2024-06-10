from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:avatar_id>/create_hot_take/', views.create_hot_take, name='create_hot_take'),
    path('<str:avatar_id>/create_post/', views.create_post, name='create_post'),
]