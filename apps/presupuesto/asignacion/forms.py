from django import forms
from presupuesto.asignacion.models import Asignacion
from helpers.FormBase import FormBase


class AsignacionForm(FormBase):

    class Meta:
        model = Asignacion
        fields = (
            "departamento",
            "presupuesto",
            "objetivo",
            "partida",
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
            "departamento": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del departamento",
                }
            ),
            "presupuesto": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "objetivo": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el objetivo",
                }
            ),
        }
