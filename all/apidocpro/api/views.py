from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import render
from school.models import Student
from rest_framework import viewsets
from .serializers import StudentSerializers
from rest_framework.serializers import Serializer as NoneSerializer
# Create your views here.

class StudentViewSet(
    generics.GenericAPIView,
    viewsets.ViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,):

    queryset = Student.objects.all()
    serializer_dict = {
        "create": StudentSerializers,
        "retrive": StudentSerializers,
        "list": StudentSerializers,
        "update": StudentSerializers,
        "delete": StudentSerializers,
    }


    def get_serializer_class(self):
        return self.serializer_dict.get(self.action, NoneSerializer)


