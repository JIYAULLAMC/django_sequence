from django.db import models

# Create your models here.





class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=20)
    marks = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}_{self.name}"