from django.contrib import admin
from .models import *


@admin.register(Comment)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content')

