from django import forms 
from emp.models import Employee,Latestnews,Calendar,JobOpening

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class latestnewsform(forms.ModelForm):
    class Meta:
        model = Latestnews
        fields = '__all__'

class calendarform(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'

class jobform(forms.ModelForm):
    class Meta:
        model = JobOpening
        fields = '__all__'

