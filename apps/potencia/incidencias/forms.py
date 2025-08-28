from potencia.incidencias.models import Incidencia
from helpers.FormBase import FormBase
from django import forms


class IncidenciaForm(FormBase):
    class Meta:
        model = Incidencia
        fields = (
            "estado",
            "sede",
            "departamento",
            "tipo_incidencia",
            "observaciones",
            "tipo_solicitud",
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
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
            "sede": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre de la sede",
                }
            ),
            "departamento": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el departamento",
                }
            ),
            "tipo_incidencia": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el tipo de incidencia",
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Describe la falla",
                }
            ),
            "tipo_solicitud": forms.Select(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el tipo de solicitud",
                }
            ),
        }
