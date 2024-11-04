import graphene

from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from app import models


class Question(DjangoObjectType):
    class Meta:
        model = models.Question
        fields = (
            "id",
            "quiz",
            "title",
        )


class Query(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.Int(required=True))
    all_quetions = graphene.List(Question)

    def resolve_question(self, info, id):
        try:
            return models.Question.objects.get(pk=id)
        except models.Question.DoesNotExist:
            return None

    def resolve_all_questions(self, info):
        return models.Question.objects.all()


schema = graphene.Schema(query=Query)
