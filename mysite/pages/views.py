from django.shortcuts import render
from .models import SubjectFile


def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')
def physics_page(request):
    files = SubjectFile.objects.filter(subject='physics')
    return render(request, 'pages/physics.html', {'files': files})

def chemistry_page(request):
    files = SubjectFile.objects.filter(subject='chemistry')
    return render(request, 'pages/chemistry.html', {'files': files})

def biology_page(request):
    files = SubjectFile.objects.filter(subject='biology')
    return render(request, 'pages/biology.html', {'files': files})
