# Sistema de Evaluaciones

Proyecto Django para registrar usuarios, iniciar sesion y administrar calificaciones de estudiantes mediante CRUD.

## Roles

- Estudiante: puede iniciar sesion y ver las calificaciones.
- Profesor: puede iniciar sesion, ver, crear, editar y eliminar calificaciones.

El registro publico crea usuarios con rol de estudiante. Las cuentas de profesor deben ser creadas o asignadas por administracion.

## Credenciales de prueba

### Profesor

```text
Usuario: profesor
Contrasena: Profesor12345
```

### Estudiante

Puedes crear un estudiante desde la opcion de registro de la aplicacion.

## Ejecutar el proyecto

```bash
python manage.py migrate
python manage.py runserver
```
