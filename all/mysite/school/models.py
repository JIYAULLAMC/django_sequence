from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.IntegerField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=20)
    marks = models.IntegerField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.sid}_{self.name}"
