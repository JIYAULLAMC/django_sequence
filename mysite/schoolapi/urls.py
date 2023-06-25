from django.urls import path, include
from schoolapi.views import StudentViewSet
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls



router = routers.DefaultRouter()

router.register("students", StudentViewSet, basename="students" )

urlpatterns = [
    path("", include(router.urls)),
    # path("schema/", SpectacularAPIView.as_view(), name='schema'),
    # path("schema/docs/", SpectacularSwaggerView.as_view(url_name='schema')),

    path("docs/", include_docs_urls(title="School API")),

    
]
