from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=600, null=False)
    created_on = models.DateTimeField(
        default=timezone.localtime(timezone.now()))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=400, null=False)
    votes = models.IntegerField(default=0)
