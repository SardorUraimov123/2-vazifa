from django.contrib import admin
from . import models
from .models import News

admin.site.register(News)
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Region)
admin.site.register(models.PostImg)
admin.site.register(models.PostVideo)
admin.site.register(models.Comment)
