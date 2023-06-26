from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework import mixins 
from school.models import Student
from schoolapi import serializers
from rest_framework.serializers import Serializer as NoneSerializers
# Create your views here.


class StudentViewSet(mixins.ListModelMixin, 
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView,
                    ViewSet):
    model = Student
    queryset = Student.objects.all()
    
    serializer_dict = {
        'list':serializers.StudentSerializer,
        'retrieve':serializers.StudentSerializer,
        'create':serializers.StudentSerializer,
        'update':serializers.StudentSerializer,
        'destroy':serializers.StudentSerializer,
    }

    def get_serializer_class(self):
        print("-------------",self.action)
        return self.serializer_dict.get(self.action, NoneSerializers )

