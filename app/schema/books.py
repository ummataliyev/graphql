"""
Books Schema
"""
import graphene

from graphene_django import DjangoObjectType

from app import models


class BookType(DjangoObjectType):
    class Meta:
        model = models.Books
        fields = (
            "id",
            "title",
            "excerpt",
        )


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)


schema = graphene.Schema(query=Query)
