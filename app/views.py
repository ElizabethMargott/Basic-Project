from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def saludo(req):
    return HttpResponse("Hello World!")

def home(req):
    context = {}
    return render(req, 'home.html', context)

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    
    return render(request, 'crear_proyecto.html', {'form': form})

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
        
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return redirect('detalle_proyecto', proyecto_id=proyecto_id)
    else:
        form = ProyectoForm(instance=proyecto)
        
    return render(request, 'editar_proyecto.html', {'form': form, 'proyecto': proyecto})

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id) 
    
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')

    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})


def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            return redirect('lista_tareas', proyecto_id=proyecto_id)
    else:
        form = TareaForm()

    return render(request, 'crear_tarea.html', {'form': form, 'proyecto': proyecto})


def listar_tareas(request):
    proyectos = Proyecto.objects.all()
    tareas = Tarea.objects.all()
    return render(request, 'listar_tareas.html', {'tareas': tareas, 'proyectos': proyectos})


def lista_tareas(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'lista_tareas.html', {'proyecto': proyecto, 'tareas': tareas})

def detalle_tarea(request):
    tarea = get_object_or_404(Tarea, pk=request.GET['tarea_id'])

    return render(request, 'detalle_tarea.html', {'tarea': tarea})

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
        return redirect('detalle_tarea', tarea_id=tarea_id)

