from django.db import models
from django.conf import settings
from django import forms
from django.forms import ModelForm
from ..account.models import CustomUser


# Create your models here.
 
     
class StudentName(models.Model):
    name = models.CharField("Prenom", max_length=30, default="")
    surname = models.CharField("Nom", max_length=30, default="")
    birthday = models.DateTimeField('Date de Naissance')
    
    def __str__(self):
        return '%s %s' % (self.name, self.surname)
    
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.name, self.surname)
    
class StudentInformation(StudentName):
    user = models.OneToOneField(CustomUser, related_name="profile", on_delete=models.CASCADE)
    nationality = models.CharField("Nationalite",
                                   max_length=50, default="française")
    address = models.CharField("Adresse",
                               max_length=200)
    phone = models.CharField("N° téléphone", 
                             max_length=10, 
                             unique=True)
    studies = models.CharField("Domaine d'études", 
                               max_length=50, 
                               choices=settings.ETUDES, 
                               default=None)
    level = models.CharField("Niveau d'études", 
                             max_length=50, 
                             choices=settings.NIVEAU, 
                             default=None)
    



# class StudentForm(ModelForm):
#     class Meta:
#         model = StudentInformations
#         fields = ['name', 'surname', 'birthday', 'email', 
#                   'address', 'phone', 'studies', 'level']
        

class StudentFilter(models.Model):
    student = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField() 
    nb_payments = models.IntegerField(choices=zip(map(str, range(1, 5)), range(1, 5)))
    
    