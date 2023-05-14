from django.shortcuts import render

# Create your views here.

from myapp.models import User, Post

from django.http import HttpResponse

def myfunc(request):
    # this is very important because
    # i have hot linked the page module to the user module 
    # event though i am able to filter page data using user module
    # make sure you have linked user module to the page user= models.Foreignkey(User)
    data = User.objects.filter(page__id=3)
    print(data)
    data = User.objects.filter(post__id=5)
    print(data)
    return HttpResponse(data)
