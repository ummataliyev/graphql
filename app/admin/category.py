"""
Answer Admin UI
"""
from django.contrib import admin

from app import models


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
