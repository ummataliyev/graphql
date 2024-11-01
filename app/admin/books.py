"""
Books Admin UI
"""
from django.contrib import admin

from app import models


@admin.register(models.Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
