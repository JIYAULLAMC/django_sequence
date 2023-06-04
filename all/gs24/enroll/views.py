from django.shortcuts import render
from . models import Student
from . forms import StudentForm, EmployeeForm
# Create your views here.


def studentinfo(request):
    print("------------------------")
    all_stus =  Student.objects.all()
    print(all_stus)
    for stu in all_stus:
        if str(stu) == "1_AAAA":
            print("-----------", stu, str(stu), )
    # setting default value or initial value
    # stu_form = StudentForm(initial={"stu_id": 100})

    # custom ordering
    # stu_form.order_fields(field_order=["stu_pass","stu_email", "stu_name", "stu_id"])
    stu_form = StudentForm()
    emp_form = EmployeeForm()
    return render(request, "enroll/studetails.html", {"stu":all_stus, "form":stu_form, "emp_form":emp_form })