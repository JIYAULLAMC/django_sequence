from django.contrib import admin

# Register your models here.

from school.models import Student, Teacher, Employee, Company


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "fees"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "salary", "date"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "area"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "emp_name", "emp_salary"]


from school.models import Cloth, Vegitable, Electronics


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cost","manufacture_date", "expiry_date"]
    
@admin.register(Vegitable)
class VegitableAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cost","manufacture_date", "expiry_date"]

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cost","manufacture_date", "expiry_date"]
    
from school.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "book_name", "book_price", "book_pages"]