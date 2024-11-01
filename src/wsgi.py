"""
WSGI config for graphql project
"""
import os

from django.core import wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = wsgi.get_wsgi_application()
