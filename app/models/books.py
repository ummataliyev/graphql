"""
Books Table
"""
from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "books"
