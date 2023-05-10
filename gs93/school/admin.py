from django.contrib import admin
from .models import Student, Teacher

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city", "marks", "pass_date"]

admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "empnum", "city", "salary", "join_date"]

admin.site.register(Teacher, TeacherAdmin)