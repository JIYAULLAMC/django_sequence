from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import StudentForm
# Create your views here.

def success(request):
    print("page submitted ---------------")
    return render(request, "enroll/success.html")



def studentinfo(request):
    print("------------------------", request.__dict__)    
    if request.method == 'POST':
        stu_form = StudentForm(request.POST)
        if stu_form.is_valid():
            stuid = stu_form.cleaned_data['stuid']
            stuname = stu_form.cleaned_data['stuname']
            stuemail = stu_form.cleaned_data['stuemail']
            stupass = stu_form.cleaned_data['stupass']
            print("--------------------", stuid, stuname, stuemail, stupass)
            stu_form = StudentForm() 
            return HttpResponseRedirect("/enroll/success/")   
            # return render(request, 'enroll/success.html')  
    else:
        stu_form = StudentForm()
    return render(request, "enroll/studetails.html", {"form":stu_form})