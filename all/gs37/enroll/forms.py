from django import forms



# class StudentForm(forms.Form):
#     stuid= forms.IntegerField(initial=123)
#     print("stuid--------------", stuid)
#     stuname = forms.CharField(max_length=50)
#     stuemail = forms.EmailField(max_length=50)
#     stupass = forms.CharField(max_length=50)
#     duration = forms.DurationField()
#     error_css_class = "error"
#     required_css_class = "required"



#     def clean_stuname(self):
#         stuname_value = self.cleaned_data['stuname']
#         if len(stuname_value) < 4:
#             raise forms.ValidationError("enter more than 4 char")
#         return stuname_value


#     def clean(self):
#         print("++++++++++++++++")
#         cleaned_data = super().clean()
#         print(cleaned_data)
#         stuemail = cleaned_data.get('stuemail')
#         if len(stuemail) < 4:
#             raise forms.ValidationError("enter more than 4 char")
        

        
      
from .models import Student
class StudentForm(forms.ModelForm):
    # stuname = forms.CharField(min_length=4)

    class Meta:
        model = Student
        fields = ["stuid", "stuname","stuemail","stupass"]
        labels = {
            "stuname" : "Enter the student name ",
            "stuemail" : "Enter the student email ",  
            } 
        error_messages = {
            "stuname": {
                "required": "Enter name properly",
                "min_length":"Min length is 4"
                },
            "stuemail": {
                "required" : "Enter the email",
                "min_length": "Min length is 4",
                }
            }
        widgets = {
            # setting the widget
            # setting the attribute
            'stuname': forms.TextInput( attrs={
                'class' : 'my_class',    
                'placeholder': 'Enter Name',
                }),
            'stupass' : forms.PasswordInput(),
        }
        