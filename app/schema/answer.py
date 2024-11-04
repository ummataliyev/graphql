import graphene

from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from app import models


class Answer(DjangoObjectType):
    class Meta:
        model = models.Answer
        fields = (
            'id',
            'question',
            'answer',
            'is_correct',
        )
