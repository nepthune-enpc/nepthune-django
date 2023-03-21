from django.shortcuts import render
import json
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.conf import settings

def signup_view(request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, 'account/signup.html', context)

def index(request):
    latest_student_list = None
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'latest_student_list': latest_student_list,
        
    }
    return render(request, 'account/authentification.html', context)
