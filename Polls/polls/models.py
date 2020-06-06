from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=600, null=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=400, null=False)
    votes = models.IntegerField(default=0)
