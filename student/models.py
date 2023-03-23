from django.db import models

# Create your models here.


class BaseStudent(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateTimeField('birth day')

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateTimeField('birth day')
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    