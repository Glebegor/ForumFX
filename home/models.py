from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class commentsTabl(models.Model):
    Text = models.TextField(verbose_name='Text')
    date = models.DateTimeField(default=timezone.now, verbose_name='date')
    avtor = models.ForeignKey(User, verbose_name='avtor', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.avtor} at {self.date}'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


    