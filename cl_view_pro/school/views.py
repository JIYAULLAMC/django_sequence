from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse


# giving the http response back to the request
class MyView(View):
    name = "Ponam"

    def get(self, request):
        return HttpResponse("<h2>this is class base view</h2>")
    
class MySubclass(MyView):

    def get(self, request):
        return HttpResponse("<h2>this how to reuse the class code!</h2>")
    

# giving the template response in class base views

class TemplateClassView(View):

    def get(self, request):
        context = {"msg": "this is context"}
        return render(request, "school/home.html", context)
    


from .forms import ContactForm

class ContactView(View):

    def get(self, request):
        form = ContactForm()

        return render(request, "school/contact.html", {"form" : form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print("-------------", name)
        return HttpResponse("the data submitted!")