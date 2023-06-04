from django.urls import path
from . import views


urlpatterns = [
    path("studs/", views.studentinfo, name="students"),
    path("success/", views.success, name="success"),
]