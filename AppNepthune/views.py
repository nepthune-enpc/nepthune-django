from django.shortcuts import render 
import json
from django.template import RequestContext

# Create your views here.

from django.http import HttpResponse
from .models import BaseStudent
from django.template import loader
from django.http import Http404
from django.conf import settings
from .forms import NameForm
from django.http import HttpResponseRedirect

def index(request):
    latest_student_list = BaseStudent.objects.order_by('-birthday')[:5]
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'latest_student_list': latest_student_list,
        
    }
    return render(request, 'AppNepthune/inscrit.html', context)

def detail(request, student_id):
    try:
        context_student =BaseStudent.objects.get(id=student_id)
    except BaseStudent.DoesNotExist:
        raise Http404("Cette élève n'est pas inscrit dans la BDD")
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        "student": context_student
    }
    return render(request, 'AppNepthune/default.html', context)

def infos_perso(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        
    context = {
        'sidebar_contents': settings.SIDEBAR_TITLES,
        'navbar_contents': settings.NAV_TITLES,
        'form': form,
    }
    return render(request, 'AppNepthune/modif-infos-persos.html', context)