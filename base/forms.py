from django import forms
from .models import employess

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employess
        fields=['name','position','department','email','phone','image']

