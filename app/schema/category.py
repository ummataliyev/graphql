import graphene

from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from app import models


class Category(DjangoObjectType):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "name",
        )
