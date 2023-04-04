from django.shortcuts import render

# Create your views here.

def scholarship_view(request):
    user = getattr(request, 'user', None)
    context = {}
    return render(request, user /"scholarships.html", context)
