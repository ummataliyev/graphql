"""
App endpoints
"""
from django.urls import path

from graphene_django.views import GraphQLView

from app import schema

urlpatterns = [
    path(
        route='quiz/',
        view=GraphQLView.as_view(
            graphiql=True,
            schema=schema.quiz.schema,
        )
    ),
]
