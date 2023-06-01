from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add any custom fields here
    pass

# class Institution(models.Model):
    
#     countries = [country for country in settings.COUNTRIES]
        
#     name = models.CharField(max_length=200)
#     country = models.CharField(max_length=20, choices=countries)
    