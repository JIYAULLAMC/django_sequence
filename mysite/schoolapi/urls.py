from django.urls import path, include
from schoolapi.views import StudentViewSet
from rest_framework import routers

from mysite.settings import SHOW_ALL_API_DOCS

router = routers.DefaultRouter()

router.register("students", StudentViewSet, basename="students" )

urlpatterns = [
    path("", include(router.urls)),
    
]
