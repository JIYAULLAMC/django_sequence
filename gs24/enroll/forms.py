from django import forms



class StudentForm(forms.Form):
    stu_id = forms.IntegerField(label="Student Id", label_suffix="------->", required=False, initial=111111111111, disabled=True, )
    stu_name = forms.CharField(initial="AAAA")
    stu_email = forms.EmailField(help_text="this is help text")
    stu_pass = forms.CharField()
    key1 = forms.CharField(widget=forms.HiddenInput())
    key2 = forms.CharField(widget=forms.HiddenInput())





class EmployeeForm(forms.Form):
    emp_id = forms.IntegerField(widget=forms.NumberInput())
    emp_name = forms.CharField(widget=forms.EmailInput())
    # emp_email = forms.EmailField(widget=forms.HiddenInput())
    emp_pass = forms.DateField(widget=forms.DateInput(attrs={'type':"datetime-local"}))
    my_choices = [('a','aaaa'),('b', 'bbbb'), ('c', 'cccc')]
    # numbers = forms.MultipleChoiceField(choices=my_choices, widget=forms.CheckboxSelectMultiple())
    nums = forms.ChoiceField(choices=my_choices, widget=forms.RadioSelect())
    numbers = forms.NullBooleanField()
    is_it = forms.CharField(widget=forms.SelectDateWidget())
