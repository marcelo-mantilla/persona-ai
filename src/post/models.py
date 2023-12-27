from django.db import models

from src.avatar.models import Avatar

# Create your models here.

class Post(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='post')

    caption = models.TextField(max_length=2500, null=False)
    action = models.TextField(max_length=2500, default=None)
    description = models.TextField(max_length=2500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.caption


class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')

    image_url = models.CharField(max_length=2000)
    image_description = models.TextField(max_length=2500)

    twitter_media_key = models.CharField(max_length=250)
    twitter_height = models.IntegerField()
    twitter_width = models.IntegerField()
    twitter_url = models.CharField(max_length=1000)
    twitter_preview_url = models.CharField(max_length=1000)

    class Meta:
        db_table = 'post_media'
