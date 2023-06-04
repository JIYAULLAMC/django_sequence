from django.contrib import admin
from school.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "marks", "city"]

admin.site.register(Student, StudentAdmin)