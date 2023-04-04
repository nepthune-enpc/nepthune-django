from django.db import models

# Create your models here.


class Scholarship(models.Model):
    
    class GrantType(models.TextChoices):
        PRIVATE = "private"
        PUBLIC = "public"
    
    provider = models.CharField("Donateur", max_length=30)
    grant_type = models.CharField("Type de bourse", choices=GrantType.choices)
    amount = models.IntegerField("Montant")
    deadline_application = models.DateField("Date limite candidature")
    
"""
deadline
date de versement
cible idéale
    age 
    niveau d'etudes
    domaine etudes

"""