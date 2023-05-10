from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "stuid", "stuname", "stuemail", "stupass", "name_pass", "view_birth_date")
    list_display_links = ("id", "stuid", "stuname",)
    actions = ["basic_action",]
    num = 10
    list_filter = ("id", "stuid", "stuname", "stuemail", "stupass")

    
    def view_birth_date(self, obj):
        return obj.stuid
    


    def name_pass(self, obj):
        return f"{obj.stuname}_{obj.stupass}"
    
    def basic_action(self, request, queryset):
        print("-----------", queryset)
        queryset.update(stuid=self.num)
        self.num = self.num+1


admin.site.register(Student, StudentAdmin)