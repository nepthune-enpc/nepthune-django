from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



class Institution(models.Model):
    
    countries = [country for country in settings.COUNTRIES.items()]
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=20, choices=countries)
    
class CustomUser(AbstractUser):
    # add any custom fields here
    is_student = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    
    
class StudentUser(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    school = models.ManyToManyField(Institution)     