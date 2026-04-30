from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistroUsuarioForm

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def listar_calificaciones(request):
    return render(request, 'calificaciones/listar.html')

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
