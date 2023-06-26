from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, UserEditForm, AdminUserEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


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
        # fm = UserChangeForm(instance=request.user)
        # custom user profile form
        if request.method == 'POST':
            if request.user.is_superuser:
                # for super user
                fm = AdminUserEditForm(request.POST, instance=request.user)
            else:
                # for normal user
                fm = UserEditForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'your profile updated successfully !!!!')
        else:
            if request.user.is_superuser:
                # for admin user
                fm = AdminUserEditForm(instance=request.user)
            else:
                # for normal user
                fm = UserEditForm(instance=request.user)
        return render(request, 'myapp/profile.html', {"name" :request.user, "form": fm})
    else:
        return HttpResponseRedirect('/login/')

# logout function view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# changing the password with old password

def user_change_pass(request):
    print("change pass -----------------")
    if request.user.is_authenticated : 
            
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # to updated the session or not get logout automatically
                update_session_auth_hash(request, request.user)
                messages.success(request, 'your credentials are updated!!!')
                return HttpResponseRedirect('/profile/')
        else: 
            fm = PasswordChangeForm(user=request.user)
        
        return render(request, 'myapp/changepass.html', {"form": fm})
    else:
        messages.success(request, 'you need to login first!!!')
        return HttpResponseRedirect("/login/")


# changing the password without old password

def user_change_pass1(request):
    print("change pass -----------------")
    if request.user.is_authenticated : 
            
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # to updated the session or not get logout automatically
                update_session_auth_hash(request, request.user)
                messages.success(request, 'your credentials are updated!!!')
                return HttpResponseRedirect('/profile/')
        else: 
            fm = SetPasswordForm(user=request.user)
        
        return render(request, 'myapp/changepass1.html', {"form": fm})
    else:
        messages.success(request, 'you need to login first!!!')
        return HttpResponseRedirect("/login/")