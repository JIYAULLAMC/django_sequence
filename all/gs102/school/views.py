from django.shortcuts import render
from school.models import Student, Book
# Create your views here.

from  django.http import HttpResponse
def home(request):

    
    res = Book.books.get_queryset()
    print("res-----------------", res)

    return HttpResponse("this is the message !")