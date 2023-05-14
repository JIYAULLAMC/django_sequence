from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from school.forms import ContactForm

# Create your views here.


# rendering the templates in the django using function base views
def myfunc(request):
    return render(request, 'school/home.html')


# rendering the templates including context
class MyView(View):

    def get(self, request):
        context = {
            "name": "Mamtaj",
            "age" : 45,
        }
        return render(request, 'school/home.html', context)


class ContactView(View):
    template_name = ""

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name , {"form": form})
    
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print("-----------------", name)
            return HttpResponse(name)
