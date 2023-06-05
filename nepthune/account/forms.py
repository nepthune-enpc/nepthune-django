from django import forms
from django.db import models, transaction
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Institution, StudentUser
from django.contrib.auth.models import User



class StudentSignupForm(UserCreationForm):
    name = forms.CharField(label="Prenom", max_length=200, required=True)
    surname = forms.CharField(label="Nom", max_length=200, required=True)
    
    email = forms.EmailField(max_length=200, help_text='Required')
    school = forms.ModelMultipleChoiceField(
        queryset=Institution.objects.all().values("name"),  widget=forms.CheckboxSelectMultiple, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('name', 'surname',  'username', 'email',  'password1', 'password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_student = True
        user.save()
        student = StudentUser.objects.create(user=user)
        return user
    
    
    class InstitutionSignupForm(UserCreationForm):
        name = forms.CharField(label="Prenom", max_length=200, required=True)
        surname = forms.CharField(label="Nom", max_length=200, required=True)
        email = forms.EmailField(max_length=200, help_text='Required')
        school = forms.ModelMultipleChoiceField(
            queryset=Institution.objects.all().values("name"),  widget=forms.CheckboxSelectMultiple, help_text='Required')

        class Meta:
            model = CustomUser
            fields = ('name', 'surname',  'username', 'email',  'password1', 'password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_institution = True
        user.save()
        institution = Institution.objects.create(user=user)
        return user