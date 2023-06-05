from django.contrib import admin
from .models import  CustomUser, Institution

# Register your models here.
admin.site.register(Institution)
admin.site.register(CustomUser)
