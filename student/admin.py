from django.contrib import admin

# Register your models here.

from .models import Student, BaseStudent

admin.site.register(BaseStudent)
admin.site.register(Student)