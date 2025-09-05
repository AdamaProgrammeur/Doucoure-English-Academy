from django.shortcuts import render, HttpResponse
from .models import Cours
# Create your views here

def acceuil(request):
    myList = [34,50,10,90]
    nom = "Adama doucoure"
    return render(request, 'acceuil.html', {'list':myList})

def course(request):
     cours = Cours.objects.all()
     return render(request, 'course.html', {'cours': cours})