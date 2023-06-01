from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    name = forms.CharField(label="Prenom", max_length=200)
    surname = forms.CharField(label="Nom", max_length=200)
    
    email = forms.EmailField(max_length=200, help_text='Required')
    # institution = forms.ChoiceField(choices=Institution.objects.all().values("name"), help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('name', 'surname',  'username', 'email',  'password1', 'password2')