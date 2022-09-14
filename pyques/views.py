from django.shortcuts import render

# Create your views here.

def simpleques(request):
    return render(request, 'pyques/simpleques.html')

def simplequesans(request):
    return render(request, 'pyques/simplequesns.html')

def oop(request):
    return render(request, 'pyques/oop.html')

def oopans(request):
    return render(request, 'pyques/oopans.html')