from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

@login_required(login_url="/account/login/")
def index(request):
    if request.user.is_authenticated:
        print("\n You are logged as {}\n".format(request.user), "\n", request)
        print("\n  \n", request.__dict__, "\n \n")
        print("\n  \n", request.__dict__.keys(), "\n \n")
        latest_student_list = StudentInformation.objects.order_by('-birthday')[:5]
        latest_student_list = StudentName.objects.order_by('-birthday')[:5]
        context = {
            'sidebar_contents': settings.SIDEBAR_TITLES,
            'navbar_contents': settings.NAV_TITLES,
            'student': latest_student_list,   
        }
        return render(request, 'student/inscrit.html', context)
    
def base(request):
    context = {
            'sidebar_contents': settings.SIDEBAR_TITLES,
            'navbar_contents': settings.NAV_TITLES,  
        }
    return render(request, 'student/tests.html', context)
    
    

def detail(request, student_id):
    try:
        context_student = StudentInformation.get(id=student_id)
    except StudentInformation.DoesNotExist:
        raise Http404("Cette élève n'est pas inscrit dans la BDD")
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        "student": context_student
    }
    return render(request, 'student/default.html', context)

def infos_perso(request):
    student_initial = StudentInformation.objects.get(username=request.user)
    if request.method == 'POST':
        if student_initial is not None:
        # create a form instance and populate it with data from the request:
            form = StudentForm(request.POST)
        else:
            form = StudentForm(request.POST, instance=student_initial)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm(instance=student_initial)
        
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'form': form,
    }
    return render(request, 'student/infos-persos.html', context)


def student_filters_view(request):
    
    # On rentre nos preferences pour la première fois
    if request.method == "POST":
        form = StudentFilterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = StudentFilterForm()
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'form': form,
    }
    return render(request, 'student/myfilters.html', context)

def modif_infos_perso(request):
    pass

def notifications_view(request):
    return render(request, 'student/notifications.html')

#################################################################
#               SCHOLARSHIPS
################################################################


def scholarships_view(request):
    pass


