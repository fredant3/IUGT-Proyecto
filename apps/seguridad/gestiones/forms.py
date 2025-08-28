from helpers.FormBase import FormBase
from seguridad.gestiones.models import Gestion
from django import forms
from django.utils import timezone
from helpers.validForm import validate_cedula


class GestionForm(FormBase):
    fecha = FormBase.create_date_field(
        "fecha",
        title="Fecha de gestión",
    )
    hora = FormBase.create_time_field(
        "hora",
        title="Hora de gestión",
    )

    class Meta:
        model = Gestion
        fields = (
            "name",
            "apellido",
            "cedula",
            "tipo",
            "descripcion",
            "fecha",
            "direccion",
            "cargo",
            "hora",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre completo",
                }
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese los apellidos"}
            ),
            "cedula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 12345678"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Detalle de la gestión...",
                    "rows": 3,
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Av. Principal, Edificio X",
                }
            ),
            "cargo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Cargo asignado"}
            ),
            "tipo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tipo de gestión",
                }
            ),
        }
        labels = {"tipo": "Tipo de Gestión", "descripcion": "Descripción Detallada"}

    def clean_fecha(self):
        data = self.cleaned_data.get("fecha")
        if data and data > timezone.now().date():
            raise forms.ValidationError("La fecha no puede ser futura")
        return data

    def clean(self):
        cleaned_data = super().clean()
        # Validación adicional si es necesario
        if cleaned_data.get("tipo") == "urgente" and not cleaned_data.get(
            "descripcion"
        ):
            self.add_error(
                "descripcion", "Las gestiones urgentes requieren descripción detallada"
            )

        return cleaned_data
