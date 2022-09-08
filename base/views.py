from django.shortcuts import render

# Create your views here.

def newproject(request):
    context = {}
    return render(request, 'base/newproject.html', context)

def interview(request):
    context = {}
    return render(request, 'base/interview.html', context)

def headcrack(request):
    context = {}
    return render(request, 'base/headcracker.html', context)

def headans(request):
    context = {}
    return render(request, 'base/headans.html', context)