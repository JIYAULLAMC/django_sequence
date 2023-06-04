from django.db import models

# Create your models here.


class Student(models.Model):
    stuid= models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.CharField(max_length=50)
    stupass = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.id}_{self.stuname}"
    