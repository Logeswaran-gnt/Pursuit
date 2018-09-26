from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=200, default="sub1")
    incharge = models.CharField(max_length=200)

class Question(models.Model):
    subject = models.ForeignKey(Subject, default="sub1")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    difficulty = models.IntegerField(default=1)


class Choice1(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

