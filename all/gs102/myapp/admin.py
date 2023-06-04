from django.contrib import admin

# Register your models here.




from myapp.models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["user", "page_name", "page_desc"]

from myapp.models import Post, Song


@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id",  "name", "description", "user"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "durantion", "written_by"]