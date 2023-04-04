from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import Student
from .forms import *

@login_required(login_url="/account/login/")
def index(request):
    if request.user.is_authenticated:
        print("\n You are logged as {}\n".format(request.user))
        latest_student_list = Student.objects.order_by('-birthday')[:5]
        context = {
            'sidebar_contents': settings.SIDEBAR_TITLES,
            'navbar_contents': settings.NAV_TITLES,
            'latest_student_list': latest_student_list,
            
        }
        return render(request, 'student/inscrit.html', context)

def detail(request, student_id):
    try:
        context_student =Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404("Cette élève n'est pas inscrit dans la BDD")
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        "student": context_student
    }
    return render(request, 'student/default.html', context)

def infos_perso(request):  
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()
        
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'form': form,
    }
    return render(request, 'student/modif-infos-persos.html', context)


