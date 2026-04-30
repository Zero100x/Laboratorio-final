from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import Calificacion


ROL_ESTUDIANTE = "estudiante"
ROL_PROFESOR = "profesor"

ROLES = (
    (ROL_ESTUDIANTE, "Estudiante"),
    (ROL_PROFESOR, "Profesor"),
)

GRUPO_ESTUDIANTES = "Estudiantes"
GRUPO_PROFESORES = "Profesores"


def asegurar_grupos_y_permisos():
    content_type = ContentType.objects.get_for_model(Calificacion)
    permisos = Permission.objects.filter(
        content_type=content_type,
        codename__in=[
            "view_calificacion",
            "add_calificacion",
            "change_calificacion",
            "delete_calificacion",
        ],
    )
    permisos_por_codigo = {permiso.codename: permiso for permiso in permisos}

    estudiantes, _ = Group.objects.get_or_create(name=GRUPO_ESTUDIANTES)
    profesores, _ = Group.objects.get_or_create(name=GRUPO_PROFESORES)

    estudiantes.permissions.set([
        permisos_por_codigo["view_calificacion"],
    ])
    profesores.permissions.set([
        permisos_por_codigo["view_calificacion"],
        permisos_por_codigo["add_calificacion"],
        permisos_por_codigo["change_calificacion"],
        permisos_por_codigo["delete_calificacion"],
    ])

    return estudiantes, profesores


def asignar_rol_usuario(user, rol):
    estudiantes, profesores = asegurar_grupos_y_permisos()

    user.groups.remove(estudiantes, profesores)
    if rol == ROL_PROFESOR:
        user.groups.add(profesores)
    else:
        user.groups.add(estudiantes)


def usuario_puede_ver_calificaciones(user):
    return user.is_superuser or user.has_perm("calificaciones_estudiantes.view_calificacion")


def usuario_puede_modificar_calificaciones(user):
    return user.is_superuser or user.has_perms([
        "calificaciones_estudiantes.add_calificacion",
        "calificaciones_estudiantes.change_calificacion",
        "calificaciones_estudiantes.delete_calificacion",
    ])
