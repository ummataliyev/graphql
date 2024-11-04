"""
Answer Admin UI
"""
from django.contrib import admin

from app import models


@admin.register(models.Answer)
class Answer(admin.ModelAdmin):
    list_display = ('answer',)
