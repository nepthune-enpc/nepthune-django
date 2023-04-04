from django.db import models
from django.conf import settings
from django import forms
from django.forms import ModelForm

# Create your models here.
 
     
class Student(models.Model):
    name = models.CharField("Nom", max_length=30)
    surname = models.CharField("Prénom", max_length=30)
    birthday = models.DateTimeField('Date de Naissance')
    email = models.EmailField("Adresse mail", max_length=30)
    address = models.CharField("Adresse", max_length=200)
    phone = models.CharField("N° téléphone", max_length=10)
    studies = models.CharField("Domaine d'études", max_length=50, choices=settings.ETUDES, default=None)
    level = models.CharField("Niveau d'études", max_length=50, choices=settings.NIVEAU, default=None)
    


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'birthday', 'email', 
                  'address', 'phone', 'studies', 'level']