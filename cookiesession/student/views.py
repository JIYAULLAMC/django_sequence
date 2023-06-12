from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.



def set_cookie(request):
    print('-------used to set the cookie')
    response = render(request, 'student/setcookie.html')

    # different ways of setting the cookie based on the various attributes
    # response.set_cookie("name", "vishwa")
    # response.set_cookie("name", "vishwa", max_age=20)
    # response.set_cookie("age", "200", max_age=20)
    # response.set_cookie("name", "vishwa", expires=datetime.utcnow()+timedelta(seconds=10))

    # signed cookies
    response.set_signed_cookie('name', 'vishwa', salt='nm', expires=datetime.utcnow()+timedelta(seconds=10))
    return response


def get_cookie(request):
    print("----------- used to get the cookie ")
    # name = request.COOKIES['name']
    # name = request.COOKIES.get("name", "Guest")
    # name = request.COOKIES.get("name")

    # getting the value of signed cookie
    name = request.get_signed_cookie('name',default="Guest", salt='nm')  # you will get the error if the session is expired
    return render(request, 'student/getcookie.html', { 'name':name})


def del_cookie(request):
    print("------------used to delet the cookie")
    response = render(request, 'student/setcookie.html')
    response.delete_cookie('name')
    return response


# sessions ---------------




def set_session(request):
    print('-------used to set the session')
    request.session['name'] = "vishwa"
    request.session['lname'] = "vishwa"
    request.session['fname'] = "vishwa"
    return render(request, 'student/setsession.html')



def get_session(request):
    print("----------- used to get the session ")
    # name = request.session['name']
    name = request.session.get("name", "Guest")
    return render(request, 'student/getcookie.html', { 'name':name})


def del_session(request):
    print("------------used to delet the session")
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')

