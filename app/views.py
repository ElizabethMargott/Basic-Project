from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def saludo(req):
    return HttpResponse("Hello World!")

def home(req):
    context = {}
    return render(req, 'home.html', context)


def lista_proyectos(request):
    proyectos = Proyecto.objects.all()

    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

