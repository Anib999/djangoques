from django.shortcuts import render

# Create your views here.

def newproject(request):
    context = {}
    return render(request, 'base/newproject.html', context)

def interview(request):
    context = {}
    return render(request, 'base/interview.html', context)