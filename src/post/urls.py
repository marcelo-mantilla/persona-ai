from django.urls import path, include

from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('create_hottake/', views.create_hottake, name='create_hottake'),
]
