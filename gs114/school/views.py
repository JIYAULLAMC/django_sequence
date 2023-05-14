from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def myfunc(request):
    return HttpResponse("<h1>function view</h1>")

from django.views import View

class MyView(View):

    def get(self, request):
        return HttpResponse("<h1>class view</h1>")

class MySubView(MyView):

    def get(self, request):
        print("mySubView------------------------")
        return super().get(request)

