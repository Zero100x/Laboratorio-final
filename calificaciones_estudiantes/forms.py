from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2")
        labels = {
            "username": "Usuario",
            "password1": "Contrasena",
            "password2": "Confirmar contrasena",
        }
        help_texts = {
            "username": "Obligatorio. Maximo 150 caracteres. Solo letras, numeros y @/./+/-/_.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Contrasena"
        self.fields["password1"].help_text = (
            "La contrasena debe tener al menos 8 caracteres, no puede ser "
            "muy similar a tus datos personales, no debe ser comun y no "
            "puede ser solo numerica."
        )
        self.fields["password2"].label = "Confirmar contrasena"
        self.fields["password2"].help_text = (
            "Escribe la misma contrasena para verificarla."
        )
