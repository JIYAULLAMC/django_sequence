from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


# rendering the templates in the django using function base views
def myfunc(request):
    return render(request, 'school/home.html')


# rendering the templates in the django using class base views
class MyView(View):

    def get(self, request):
        return render(request, 'school/home.html')



