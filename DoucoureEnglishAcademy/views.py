from django.shortcuts import render, HttpResponse
from .models import Cours
# Create your views here

def acceuil(request):
    return render(request, 'acceuil.html')

def course(request):
     cours = Cours.objects.all()
     return render(request, 'course.html', {'cours': cours})