from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion


def inicio(request):
    return render(request, 'inicio.html')


@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.order_by('-id')
    return render(
        request,
        'calificaciones/listar.html',
        {'calificaciones': calificaciones},
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


@login_required
def editar_calificacion(request, calificacion_id):
    calificacion = get_object_or_404(Calificacion, pk=calificacion_id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CalificacionForm(instance=calificacion)

    return render(
        request,
        'calificaciones/editar.html',
        {'form': form, 'calificacion': calificacion},
    )


@login_required
def eliminar_calificacion(request, calificacion_id):
    calificacion = get_object_or_404(Calificacion, pk=calificacion_id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar')
    return redirect('listar')


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
