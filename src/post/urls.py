from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_life_post, name='create_life_post')
]
