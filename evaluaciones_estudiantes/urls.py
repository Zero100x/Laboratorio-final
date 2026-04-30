from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from calificaciones_estudiantes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),

    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('calificaciones/', include('calificaciones_estudiantes.urls')),
]