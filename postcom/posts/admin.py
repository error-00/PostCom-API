from django.contrib import admin
from .models import *


@admin.register(Post)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')

