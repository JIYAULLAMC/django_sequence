from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


# rendering the templates in the django using function base views
def myfunc(request):
    return render(request, 'school/home.html')


class MyHome(TemplateView):
    template_name="school/home.html"


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = "jiya"
        context['age'] = 12
        print("kwargs", kwargs)
        context['id']= kwargs['id']
        context['msg']= kwargs['msg']
        # context = {"name" : "jiya", "age": 12}
        return  context





