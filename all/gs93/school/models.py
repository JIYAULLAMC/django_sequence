from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    pass_date = models.DateField()

    def __str__(self):
        return f"name: {self.name} roll: {self.roll} city: {self.city} marks: {self.marks} pass_date: {self.pass_date}"


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=50)
    salary = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return f"name: {self.name} roll: {self.roll} city: {self.city} marks: {self.marks} pass_date: {self.pass_date}"