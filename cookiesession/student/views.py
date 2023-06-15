from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
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

    # how toset the expiry in seconds 
    request.session.set_expiry(10)
    
    # setting the test cookie
    request.session.set_test_cookie()
    return render(request, 'student/setsession.html')



def get_session(request):
    print("----------- used to get the session ")
    # name = request.session['name']
    name = request.session.get("name", "Guest")
    keys = request.session.keys
    print("-----------", keys)
    # used to set the session using setdefault
    # request.session.setdefault("age", 34)

    # information about session

    print("------------", request.session.get_session_cookie_age())
    print("----------", request.session.get_expiry_age())
    print("--------", request.session.get_expiry_date())
    print("--------", request.session.get_expire_at_browser_close())


    # confirming the test cookie worked on not
    print("worked", request.session.test_cookie_worked())
    return render(request, 'student/getsession.html', { 'name':name, 'keys' : keys })


def del_session(request):
    print("------------used to delet the session data")
    if 'name' in request.session:
        del request.session['name']
    # used to remove the whole session -> inspect in application and check
    # request.session.flush()

    # to remove the expired session
    request.session.clear_expired()

    # removing the test cookie
    request.session.delete_test_cookie()
    return render(request, 'student/delsession.html')

