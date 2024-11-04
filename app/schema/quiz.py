import graphene

from graphene_django import DjangoListField
from graphene_django import DjangoObjectType

from app import models


class Quiz(DjangoObjectType):
    class Meta:
        model = models.Quiz
        fields = (
            'id',
            'title',
        )


class Query(graphene.ObjectType):
    quiz = graphene.Field(Quiz, id=graphene.Int(required=True))
    all_quizzes = graphene.List(Quiz)

    def resolve_quiz(self, info, id):
        try:
            return models.Quiz.objects.get(pk=id)
        except models.Quiz.DoesNotExist:
            return None

    def resolve_all_quizzes(self, info):
        return models.Quiz.objects.all()


schema = graphene.Schema(query=Query)
