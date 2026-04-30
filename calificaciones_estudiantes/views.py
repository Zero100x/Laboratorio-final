from django.shortcuts import render

<<<<<<< origin/feature-create-calificaciones
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
=======
from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion
>>>>>>> local

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def listar_calificaciones(request):
<<<<<<< origin/feature-create-calificaciones
    return render(request, 'calificaciones/listar.html')
=======
    calificaciones = Calificacion.objects.order_by('-id')
    return render(request, 'calificaciones/listar.html', {'calificaciones': calificaciones})


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
>>>>>>> local
