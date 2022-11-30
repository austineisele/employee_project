from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    #to inherit another class you'll use "Meta"
    class Meta:
        model = Employee
        #here is where you would add the fields. You can do '__all__' or a tuple
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname':'Full Name',
            'mobile': 'Phone Number',
            'emp_code': 'EMP.Code'
        }
    
    #here is how you can put a default value for the forms.
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required =  False
