# Create your views here.
from django.shortcuts import render, redirect
from .forms import CursoForm, EstudianteForm, ProfesorForm
from .models import Curso, Estudiante, Profesor
from django.db.models import Q

def inicio(request):
    search_query = request.GET.get('search_query')
    cursos = None

    if search_query:
        cursos = Curso.objects.filter(Q(nombre__icontains=search_query) | Q(comision=search_query))

    return render(request, 'AppCentu/inicio.html', {'cursos': cursos, 'search_query': search_query})

def curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redireccionar a la sección de inicio después de enviar el formulario
    else:
        form = CursoForm()
    return render(request, 'AppCentu/curso.html', {'form': form})

def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redireccionar a la sección de inicio después de enviar el formulario
    else:
        form = EstudianteForm()
    return render(request, 'AppCentu/estudiantes.html', {'form': form})

def profesores(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redireccionar a la sección de inicio después de enviar el formulario
    else:
        form = ProfesorForm()
    return render(request, 'AppCentu/profesores.html', {'form': form})
