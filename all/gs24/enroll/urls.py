from django.urls import path
from . import views


urlpatterns = [
    path("studs/", views.studentinfo, name="students"),
]