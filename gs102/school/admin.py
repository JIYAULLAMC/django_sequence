from django.contrib import admin

# Register your models here.

from school.models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "fees"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "salary", "date"]