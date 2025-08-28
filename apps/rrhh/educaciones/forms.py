from django import forms
from rrhh.educaciones.models import Educacion
from helpers.FormBase import FormBase


class EducacionForm(FormBase):
    fecha_inicio = FormBase.create_date_field(
        "fecha_inicio",
        title="Fecha de Inicio",
    )
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion",
        title="Fecha de Culminación",
    )

    class Meta:
        model = Educacion
        fields = (
            "colegio",
            "codigo_titulo",
            "titulo",
            "area_conocimiento",
            "fecha_inicio",
            "fecha_culminacion",
            "enlace_certificado",
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
            "colegio": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Universidad Central de Venezuela",
                }
            ),
            "codigo_titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: T-2023-001"}
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Licenciatura en Administración",
                }
            ),
            "area_conocimiento": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Ciencias Administrativas",
                }
            ),
            "enlace_certificado": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://ejemplo.com/certificado.pdf",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_inicio and fecha_culminacion:
            if fecha_culminacion < fecha_inicio:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de inicio",
                )

        return cleaned_data
