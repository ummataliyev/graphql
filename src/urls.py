"""
URL configuration for graphql project
"""
from django.urls import path
from django.urls import include
from django.contrib import admin

from app import endpoints


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(endpoints)),
]
