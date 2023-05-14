from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


# rendering the templates in the django using function base views
def myfunc(request):
    return render(request, 'school/home.html')


class MyHome(TemplateView):
    template_name="school/home.html"





