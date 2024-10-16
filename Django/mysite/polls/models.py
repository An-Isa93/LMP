import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    time = models.TimeField("time published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        published_datetime = datetime.datetime.combine(self.pub_date, self.time)
        return published_datetime >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
