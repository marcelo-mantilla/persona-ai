# Generated by Django 4.2.8 on 2023-12-27 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_action_alter_post_caption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('image_description', models.TextField(max_length=2500)),
                ('twitter_media_key', models.CharField(max_length=250)),
                ('twitter_height', models.IntegerField()),
                ('twitter_width', models.IntegerField()),
                ('twitter_url', models.CharField(max_length=1000)),
                ('twitter_preview_url', models.CharField(max_length=1000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='post.post')),
            ],
            options={
                'db_table': 'post_media',
            },
        ),
    ]