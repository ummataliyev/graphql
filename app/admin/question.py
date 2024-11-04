"""
Answer Admin UI
"""
from django.contrib import admin

from app import models


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = ('title',)
