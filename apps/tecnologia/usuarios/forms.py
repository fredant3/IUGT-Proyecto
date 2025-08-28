from django.forms import (
    BooleanField,
    CheckboxInput,
    CharField,
    SelectMultiple,
    ModelMultipleChoiceField,
    TextInput,
    PasswordInput,
    ChoiceField,
    Select,
)
from django.contrib.auth.models import Group, Permission
from users.auth.models import User
from helpers.FormBase import FormBase
from django.core.validators import MinLengthValidator, MaxLengthValidator
from helpers.models import BOOLEAN_CHOICES
from django.contrib.auth.hashers import make_password


class UserForm(FormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, "empleado"):
            self.fields["nombre_empleado"].initial = (
                f"{self.instance.empleado.nombres} {self.instance.empleado.apellidos}"
            )

        if self.instance.pk:
            self.fields["groups"].initial = self.instance.groups.all()
            self.fields["user_permissions"].initial = (
                self.instance.user_permissions.all()
            )

        self.fields["user_permissions"].queryset = Permission.objects.exclude(
            content_type__app_label__in=["auth", "admin", "sessions", "contenttypes"]
        )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password and self.instance.pk:
            return self.instance.password
        return make_password(password)

    is_active = ChoiceField(
        choices=BOOLEAN_CHOICES,
        widget=Select,
        label="Activo",
    )

    nombre_empleado = CharField(
        label="Nombre del Empleado",
        required=False,
        widget=TextInput(attrs={"readonly": "readonly"}),
    )

    groups = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=SelectMultiple(attrs={"class": "dual-listbox"}),
        label="Grupos",
    )

    user_permissions = ModelMultipleChoiceField(
        queryset=Permission.objects.filter(
            content_type__app_label__in=["tu_app", "otras_apps_relevantes"]
        ),
        required=False,
        widget=SelectMultiple(attrs={"class": "dual-listbox"}),
        label="Permisos personalizados",
    )

    password = CharField(
        label="Contraseña",
        widget=PasswordInput(
            attrs={"placeholder": "Contraseña", "class": "input__input"}
        ),
        max_length=15,
        required=False,
        validators=[MinLengthValidator(6), MaxLengthValidator(15)],
    )

    class Meta:
        model = User
        fields = (
            "nombre_empleado",
            "username",
            "is_active",
            "password",
        )
        labels = {
            "username": "Usuario",
            "dni": "DNI",
            "password": "Contraseña",
        }
        widgets = {
            "username": TextInput(attrs={"placeholder": "Usuario"}),
            "dni": TextInput(attrs={"placeholder": "DNI"}),
        }
