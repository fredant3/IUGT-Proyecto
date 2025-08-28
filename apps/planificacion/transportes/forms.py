from django import forms
from planificacion.transportes.models import Transporte
from helpers.FormBase import FormBase


class TransporteForm(FormBase):
    class Meta:
        model = Transporte
        fields = (
            "estado",
            "mes",
            "transporte",
            "cantidad",
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
        labels = {
            "estado": "Estado del transporte",
            "mes": "Mes de operación",
            "transporte": "Tipo de transporte",
            "cantidad": "Cantidad de unidades",
        }
        widgets = {
            "transporte": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Tipo de transporte",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Cantidad de unidades",
                    "min": "0",
                }
            ),
        }
