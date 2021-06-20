from django.db import models


# Create your models here.
from django.utils import timezone
import datetime


class Question(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date >= (timezone.now() - datetime.timedelta(days=2)).timestamp()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

