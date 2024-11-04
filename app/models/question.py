from django.db import models

from app.models import quiz


class Question(models.Model):
    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(
        to=quiz.Quiz,
        on_delete=models.DO_NOTHING
    )
    technique = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField(
        choices=SCALE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'
