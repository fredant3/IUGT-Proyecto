from django import forms
from administracion.tipo_averia.models import TipoAveria
from helpers.FormBase import FormBase


class TipoAveriaForm(FormBase):
    class Meta:
        model = TipoAveria
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: bueno",
                    "minlength": 3,
                    "maxlength": 200,
                }
            )
        }
