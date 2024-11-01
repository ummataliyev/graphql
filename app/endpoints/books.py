"""
App endpoints
"""
from django.urls import path

from graphene_django.views import GraphQLView

from app import schema

urlpatterns = [
    path(
        route='graphql/',
        view=GraphQLView.as_view(
            graphiql=True,
            schema=schema.books.schema)
    ),
]
