from django.contrib import admin
from .models import StudentName, StudentInformation, StudentFilter
# Register your models here.


admin.site.register(StudentName)
admin.site.register(StudentInformation)
admin.site.register(StudentFilter)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')