from django.shortcuts import render

# Create your views here.

from .forms import UserForm
from .models import User

def regi(request):

    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid:
            fm.save()
    else:
        fm =UserForm()
    return render(request, 'enroll/userregister.html', {'form' : fm})
