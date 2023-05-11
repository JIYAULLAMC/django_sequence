from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True


class Student(CommonInfo):
    date = None
    fees = models.IntegerField()

class Teacher(CommonInfo):
    salary = models.IntegerField()
    date = models.DateTimeField()





class Company(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)


class Employee(Company):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.IntegerField()


    