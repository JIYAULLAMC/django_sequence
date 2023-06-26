from rest_framework.routers import DefaultRouter
from django.urls import path, include
from school.models import Student
from .views import StudentViewSet
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

router.register("students", StudentViewSet, basename='students')


urlpatterns = [
    path("",  include(router.urls)),
    path("docs/", include_docs_urls(title="School API")),

]