from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.


def home(request):
    return render(request, 'enroll/course.html')


# example for the perview cache

@cache_page(30)
def myhome(request):
    return render(request, 'enroll/mycourse.html')


def temp(request):
    return render(request, "enroll/temp.html")


# low level cache to cache the python data types which will not change frequently

from django.core.cache import cache


# this how to get or set the cache

# def low_level(request):
#     f_name = cache.get('name', 'guest')
#     if f_name == 'guest':
#         cache.set('name', 'nazeer ahmed', 30)
#         f_name = cache.get('name')
#     return render(request, 'enroll/lowlevel.html' ,{"fm":f_name})

# f_name = cache.get_or_set('name', "Md jiyaulla", 30, version=2)
# def low_level(request):
#     f_name = cache.get_or_set('name', "jiyaulla", 30)
#     return render(request, 'enroll/lowlevel.html' ,{"fm":f_name})


# how to set many data at a time
# def low_level(request):
#     data = {'name' : "jiya", "age":100}
#     cache.set_many(data)
#     data = cache.get_many(data)
#     return render(request, 'enroll/lowlevel.html' ,{"data": data})


# how to remove the data from the cache
def low_level(request):
    data = {'name' : "jiya", "age":100}
    cache.set_many(data)
    # data = cache.delete('name')  #incr or decr to increase and decrese the data clear used to remove the cache
    # clear is used to remove all the cache
    # data = cache.delete('name', version=2)
    return render(request, 'enroll/lowlevel.html' ,{"data": data})