from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Avg                  

from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion


def inicio(request):
    return render(request, 'inicio.html')


@login_required
def listar_calificaciones(request):
    calificaciones   = Calificacion.objects.order_by('-id')
    promedio_general = Calificacion.objects.aggregate(  
                           Avg('promedio')
                       )['promedio__avg']               
    return render(
        request,
        'calificaciones/listar.html',
        {
            'calificaciones':   calificaciones,
            'promedio_general': promedio_general or 0,  
        },
    )


@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})