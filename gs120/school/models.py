from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    marks = models.IntegerField()
    city = models.CharField(max_length=50)