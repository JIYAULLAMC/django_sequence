from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from school.models import Student
# Create your views here.


class StudentList(ListView):
    model = Student
    context_object_name = "students"
    ordering = "-age"


    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(age__lt=23)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["name"] = "jiyaulla"
        return context

class StudentDetail(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "school/home.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["students"] = self.model.objects.all()
        return context
    



