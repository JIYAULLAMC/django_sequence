from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from .forms import UserForm
from .models import User

def regi(request):

    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid:
            fm.save()
            print("-----------", messages.get_level(request))
            messages.set_level(request, messages.SUCCESS)
            messages.add_message(request, messages.SUCCESS, "your account has been created!")
            print("-----------", messages.get_level(request))
            messages.set_level(request, messages.INFO)
            messages.add_message(request, messages.INFO, "your account has been created!")
            print("-----------", messages.get_level(request))
            messages.set_level(request, messages.WARNING)
            messages.add_message(request, messages.WARNING, "your account has been created!")
            print("-----------", messages.get_level(request))
            messages.add_message(request, messages.ERROR, "your account has been created!")
            messages.set_level(request, messages.ERROR)
            print("-----------", messages.get_level(request))
            messages.success(request, "your success account has been created!")
            messages.info(request, "your info account has been created!")
            messages.warning(request, "your  warning account has been created!")
            messages.error(request, "your error account has been created!")

    else:
        fm =UserForm()
    return render(request, 'enroll/userregister.html', {'form' : fm})
