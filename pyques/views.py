from django.shortcuts import render

# Create your views here.

def simpleques(request):
    return render(request, 'pyques/simpleques.html')