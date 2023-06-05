from django.shortcuts import render, redirect
import json
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.conf import settings
from django.views.decorators.csrf import requires_csrf_token,  csrf_protect, csrf_exempt
from .forms import StudentSignupForm
from ..student.models import StudentInformation


def first_page_view(request):
    return render(request, 'account/authenticate.html')

# @csrf_exempt
@requires_csrf_token
def student_signup_view(request):
    print(request.__dict__)
    if request.method == "POST":
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            # Save to the BDD
            user = form.save()
            # Log the user in
            login(user, request)
            return redirect("student:index")
    else:
        form = StudentSignupForm()
    context = {"form": form}
    return render(request, 'account/signup.html', context)

# @csrf_exempt
@requires_csrf_token
def institution_signup_view(request):
    if request.method == "POST":
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            # Save to the BDD
            user = form.save()
            # Log the user in
            login(user, request)
            return redirect("student:index")
    else:
        form = StudentSignupForm()
    context = {"form": form}
    return render(request, 'account/signup.html', context)

@csrf_exempt
def login_view(request):
    print("\n", request, "\n \n \n")
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        form = AuthenticationForm(data=request.POST)
        print(username, password)
        print("\n FORM VALIDITY:", form.get_user(), form.is_bound, form.errors, form.is_valid())
        if form.is_valid():
            # log in the user 
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("student:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "account/login.html", context)

@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("account:login")
    return
        

def index(request):
    latest_student_list = None
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'latest_student_list': latest_student_list,
        
    }
    return render(request, 'account/authentification.html', context)


def project_view(request):
    return render(request, 'account/le_projet.html')

def purpose_view(request):
    return render(request, 'account/a_propos.html')

def act_view(request):
    return render(request, 'account/agir.html')
