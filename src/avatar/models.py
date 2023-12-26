from django.db import models
from src.user.models import User
# import PromptTemplate


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avatars')

    # Facebook

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'avatar'


class PersonaTemplate(models.Model):
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, related_name='persona_template', primary_key=True)

    personality = models.CharField(max_length=1000, null=True, blank=True)
    audience = models.CharField(max_length=1000, null=True, blank=True)
    vision = models.CharField(max_length=1000, null=True, blank=True)
    purpose = models.CharField(max_length=1000, null=True, blank=True)
    values = models.CharField(max_length=1000, null=True, blank=True)
    additional_info = models.CharField(max_length=1000, null=True, blank=True)
    career = models.CharField(max_length=1000, null=True, blank=True)
    hobbies = models.CharField(max_length=1000, null=True, blank=True)
    tone = models.CharField(max_length=1000, null=True, blank=True)
    summary = models.CharField(max_length=1000, null=True, blank=True)
    # location

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'avatar_persona_template'

    FIELD_TO_TITLES = {
        'personality': 'Personality',
        'audience': 'Audience',
        'vision': 'Vision',
        'purpose': 'Purpose',
        'values': 'Values',
        'additional_info': 'Additional Info',
        'career': 'Career',
        'hobbies': 'Hobbies',
        'tone': 'Tone',
        # 'summary' is LLM generated
    }

    def as_prompt(self):
        persona_string = "**Avatar Persona**\n\n"
        for field, title in self.FIELD_TO_TITLES.items():
            value = getattr(self, field, None)
            if value:
                persona_string += f"{title}: \n{value}\n\n"
        return persona_string


class CaptionTemplate(models.Model):
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, related_name='caption_template', primary_key=True)

    caption_theme = models.CharField(max_length=1000, blank=True)
    caption_length = models.IntegerField(blank=True, null=True, default=None)
    example_captions = models.CharField(max_length=1000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'avatar_caption_template'

    FIELD_TO_TITLES = {
        'caption_theme': 'Caption Theme',
        'example_captions': 'Example Captions',
    }

    def as_prompt(self):
        caption_string = "**Caption Theme**\n\n"
        for field, title in self.FIELD_TO_TITLES.items():
            value = getattr(self, field, None)
            if value:
                caption_string += f"{title}: \n{value}\n\n"
        return caption_string


class ImageTemplate(models.Model):
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, related_name='image_template', primary_key=True)
    visual_style = models.CharField(max_length=1000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'avatar_image_template'

    FIELD_TO_TITLES = {
        'visual_style': 'Visual Style',
    }

    def as_prompt(self):
        image_string = "**DALL-E 3 Image Aesthetic**\n\n"
        for field, title in self.FIELD_TO_TITLES.items():
            value = getattr(self, field, None)
            if value:
                image_string += f"{title}: \n{value}\n\n"
        return image_string
