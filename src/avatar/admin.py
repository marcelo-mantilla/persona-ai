from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Avatar)
admin.site.register(PersonaTemplate)
admin.site.register(CaptionTemplate)
admin.site.register(ImageTemplate)