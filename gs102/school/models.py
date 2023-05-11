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



# proxy model example
# data wil be remain same but the behaiver will be change

class Product(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    manufacture_date = models.DateField()
    expiry_date = models.DateField()



class Cloth(Product):
    class Meta:
        proxy = True
        ordering = ["id"]


class Vegitable(Product):
    class Meta:
        proxy = True
        ordering = ["name"]


class Electronics(Product):
    class Meta:
        proxy = True
        ordering = ["manufacture_date"]




class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_price = models.IntegerField()
    book_pages = models.IntegerField()

    books = models.Manager()
