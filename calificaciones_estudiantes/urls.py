from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_calificaciones, name='listar'),
]