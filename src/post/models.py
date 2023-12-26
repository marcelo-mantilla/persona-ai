from django.db import models

from src.avatar.models import Avatar

# Create your models here.

class Post(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='post')

    image_url = models.CharField(max_length=2000)
    image_description = models.TextField(max_length=2500)
    caption = models.TextField(max_length=2500)
    action = models.TextField(max_length=2500, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.caption
