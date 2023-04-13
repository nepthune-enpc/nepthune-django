from django import forms
from .models import *
# from ..config import constants
from django.conf import settings
from django.forms import ModelForm


class StudentForm(ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['name', 'surname', 'birthday', 'email', 
                  'address', 'phone', 'studies', 'level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class StudentFilterForm(ModelForm):
    class Meta:
        model = StudentFilter
        fields = ['amount', 'payment_date', 'nb_payments']
        # widgets = {'nb_payments': forms.MultipleChoiceField(choices=zip(map(str, range(1, 5)), range(1, 5)),
        #                                     required=False, 
        #                                     label="Nombre limite de Versements",
        #                                     widget=forms.RadioSelect) }
        

class NameForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': "Prénom", 'style':"width:300px;", 'class':'form-control'}))
    surname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': "Nom", 'style':"width:300px;", 'class':'form-control'}))
    birthday = forms.DateTimeField(widget=forms.SelectDateWidget(years=[str(i) for i in range(1900, 2023)], attrs={ 'style':"max-width:300px;"}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'placeholder': "adresse mail", 'style':"max-width:300px;", 'class':'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "ex: 270 rue Saint-Jacques 75005 Paris", 'style':"max-width:300px;", 'class':'form-control'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': "Téléphone", 'style':"max-width:300px; height:30px;", 'class':'form-control'}))
    studies = forms.ChoiceField(label="Domaine d'études", widget=forms.RadioSelect, choices=settings.ETUDES)
    level = forms.ChoiceField(label="Niveau d'études", widget=forms.RadioSelect, choices=settings.NIVEAU)

        