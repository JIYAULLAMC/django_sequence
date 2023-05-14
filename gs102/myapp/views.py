from django.shortcuts import render

# Create your views here.

from myapp.models import User, Post

from django.http import HttpResponse

def myfunc(request):
    data = User.objects.filter(page__id=3)
    print(data)
    data = User.objects.filter(post__id=5)
    print(data)
    return HttpResponse(data)
