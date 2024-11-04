from django.db import models

from app.models import question


class Answer(models.Model):
    question = models.ForeignKey(
        to=question.Question,
        on_delete=models.DO_NOTHING
    )
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'
