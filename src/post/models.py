from django.db import models

from src.avatar.models import Avatar

# Create your models here.

class Post(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='post')

    image_url = models.CharField(max_length=200)
    image_description = models.CharField(max_length=1000)
    caption = models.CharField(max_length=1000)
    action = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.caption
