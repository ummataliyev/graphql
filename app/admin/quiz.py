"""
Answer Admin UI
"""
from django.contrib import admin

from app import models


@admin.register(models.Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ('title',)
