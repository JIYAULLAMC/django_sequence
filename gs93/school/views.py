from django.shortcuts import render
from school.models import Student, Teacher
# Create your views here.
import datetime
from datetime import date, time

def home(request):
    # students_data = Student.objects.all()
    today_date = datetime.datetime.now().date()
    # print("---------------------", today_date, str(today_date))
    # students_data = Student.objects.filter(marks=90, pass_date="2023-05-07")
    # students_data = Student.objects.exclude(marks=90, pass_date=today_date)
    # students_data = Student.objects.order_by("city")
    # students_data = Student.objects.order_by("?")
    # students_data = Student.objects.values()
    # students_data = Student.objects.values("id", "name") 
    # students_data = Student.objects.values_list() 
    # students_data = Student.objects.values_list("id", 'name', 'city', named=True) 
    # students_data = Student.objects.dates('pass_date', 'day') 

    # qs1 = Student.objects.values_list("id", "name")
    # qs2 = Teacher.objects.values_list("id", "name")
    # students_data = qs1.union(qs2)
    # students_data = qs1.union(qs2, all=True)
    # students_data = qs1.intersection(qs2)
    # students_data = qs1.difference(qs2)
    # students_data = qs2.difference(qs1)
    
    # return queryset using single object
    # return render(request, "school/home.html", {"students": students_data})

    # student = Student.objects.get(pk=1)
    # student = Student.objects.first()
    # student = Student.objects.order_by("pass_date").first()
    # student = Student.objects.last()
    # student = Student.objects.order_by("city").last()
    # student = Student.objects.latest("name")
    # student = Student.objects.filter(city="bbbb").first()
    # student = Student.objects.filter(city="bbbb").last()
    # student = Student.objects.filter(city="bbbb").latest("name")
    # student = Student.objects.filter(city="bbbb").earliest("name")
    # student = Student.objects.earliest("name")

    # students = Student.objects.all().exists()
    # students = Student.objects.filter(name="xxxx").exists()


    # students = Student.objects.all()
    # stu = Student.objects.get(pk=1)
    # print("++++++++++++++", students.filter(pk=stu.pk).exists())

    # student = {
    #     "id" : 11,
    #     "name" : "KKKK",
    #     "roll" : 12,
    #     "city" : "haveri",
    #     "marks" : 95,
    #     "pass_date" : "2023-05-08", 
    # }

    # # students = Student.objects.create(**student)

    # # students = Student.objects.filter(id=10).update(name="jiya")
    # students = Student.objects.update_or_create(**student)

    # stu_objs = [
    #     Student(name="JJJJ", roll=13, city="bengaluru", marks=89, pass_date="2023-05-08"),
    #     Student(name="MMMM", roll=14, city="bankapur", marks=90, pass_date="2023-05-01"),
    #     Student(name="NNNN", roll=15, city="hubballi", marks=94, pass_date="2023-05-01"),
    # ]
    # students = Student.objects.bulk_create(stu_objs)

    # all_students = Student.objects.filter(city="bbbb")

    # for stu_obj in all_students:
    #     stu_obj.city="bhell"

    # students = Student.objects.bulk_update(all_students, ["city"])

    # students = Student.objects.in_bulk([1,2])

    # students = Student.objects.get(pk=10).delete()
    # # students = Student.objects.all().delete()

    # students = Student.objects.filter(name__exact='AAAA')
    # students = Student.objects.filter(name__iexact="AAAA") 
    # students = Student.objects.filter(name__contains="a") 
    # students = Student.objects.filter(name__contains="A") 
    # students = Student.objects.filter(city__icontains="a") 
    # students = Student.objects.filter(name__icontains="a") 

    # students = Student.objects.filter(marks__in=[ 97, 95]) 
    # students = Student.objects.filter(marks__gt=97) 
    # students = Student.objects.filter(marks__gte=97) 
    # students = Student.objects.filter(marks__lt=90) 
    # students = Student.objects.filter(marks__lte=90) 
    # students = Student.objects.filter(name__startswith='A') 
    # students = Student.objects.filter(name__istartswith='a') 
    # students = Student.objects.filter(name__iendswith='a') 
    # students = Student.objects.filter(name__iendswith='A') 
    # students = Student.objects.filter(pass_date__range= ('2023-05-01', '2023-05-04'))
    
    # applicable for the datetime object
    # students = Student.objects.filter(pass_date__date = datetime.datetime.date(2023, 5,5))
    # students = Student.objects.filter(pass_date__year=2022)
    # students = Student.objects.filter(pass_date__year__gt=2022)
    # students = Student.objects.filter(pass_date__year__gte=2022)
    # students = Student.objects.filter(pass_date__month__gte=4)
    # students = Student.objects.filter(pass_date__day=2)
    # students = Student.objects.filter(pass_date__day__gte=2)
    # students = Student.objects.filter(pass_date__week=2)
    # students = Student.objects.filter(pass_date__week__gte=2)
    # students = Student.objects.filter(pass_date__week_day=5)
    # students = Student.objects.filter(pass_date__week_day__gte=5)
    # students = Student.objects.filter(pass_date__quarter=1)
    # students = Student.objects.filter(pass_date__quarter__gte=3)
    # students = Student.objects.filter(pass_date__time = time(8.00))
    # students = Student.objects.filter(pass_date__time__range = time(8.00))
    
    # students = Student.objects.filter(pass_date__hours = 8)
    # students = Student.objects.filter(pass_date__hours__range = (1, 7))
    
    # students = Student.objects.filter(pass_date__minutes = 20)
    # students = Student.objects.filter(pass_date__minutes__range = (30, 50))
    
    # students = Student.objects.filter(pass_date__seconds = 20)
    # students = Student.objects.filter(pass_date__seconds__range = (1, 20))
    # students = Student.objects.filter(roll_isnull=True)
    
    # print("++++++++++++++++++",students)
    # print("+++++++++++", students.query)

    return render(request, "school/home.html", {"student": students})


