from django.contrib import admin

# Register your models here.




from myapp.models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["user", "page_name", "page_desc"]