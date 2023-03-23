from django import forms
from . import models

class NameForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    birthday = forms.DateTimeField()
    email = forms.EmailField(max_length=30)
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=10)
    
    
# class CreateScholarship(forms.ModelForm):
#     class Meta:
        