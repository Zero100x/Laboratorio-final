from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion
from .permisos import (
    asegurar_grupos_y_permisos,
    usuario_puede_modificar_calificaciones,
    usuario_puede_ver_calificaciones,
)


def inicio(request):
    return render(request, 'inicio.html')


@login_required
def listar_calificaciones(request):
    asegurar_grupos_y_permisos()
    if not usuario_puede_ver_calificaciones(request.user):
        return redirect('inicio')

    calificaciones = Calificacion.objects.order_by('-id')
    promedio_general = Calificacion.objects.aggregate(
        Avg('promedio')
    )['promedio__avg']
    puede_modificar = usuario_puede_modificar_calificaciones(request.user)

    return render(
        request,
        'calificaciones/listar.html',
        {
            'calificaciones': calificaciones,
            'promedio_general': promedio_general or 0,
            'puede_modificar': puede_modificar,
        },
    )


@login_required
def crear_calificacion(request):
    asegurar_grupos_y_permisos()
    if not request.user.has_perm("calificaciones_estudiantes.add_calificacion"):
        return redirect('listar')

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
    asegurar_grupos_y_permisos()
    if not request.user.has_perm("calificaciones_estudiantes.change_calificacion"):
        return redirect('listar')

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
    asegurar_grupos_y_permisos()
    if not request.user.has_perm("calificaciones_estudiantes.delete_calificacion"):
        return redirect('listar')

    calificacion = get_object_or_404(Calificacion, pk=calificacion_id)
    if request.method == 'POST':
        calificacion.delete()
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
