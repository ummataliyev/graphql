from django.db import models

from app.models import category


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        to=category.Category,
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        db_table = 'quiz'
