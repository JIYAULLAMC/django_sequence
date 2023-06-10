from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# sign up function base view
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        print("---------------")
        if fm.is_valid() :
            fm.save()
            messages.success(request, 'your data created succeefully')
    else:
        fm = SignUpForm()    
    return render(request,"myapp/signup.html",{ "form" : fm})


# log in function base view
def user_login(request):

    if not request.user.is_authenticated : 

        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                print("==============", user)
                if user:
                    print("----------", login(request, user))
                    messages.success(request, 'your credentials are created!!!')
                    return HttpResponseRedirect("/profile/")
        else:
            fm = AuthenticationForm()
            print("--------------------")
        return render(request, 'myapp/userlogin.html', {"form" : fm })

    else:
        return HttpResponseRedirect("/profile/")
# Profile function view
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/profile.html', {"name" :request.user})
    else:
        return HttpResponseRedirect('/login/')

# logout function view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')