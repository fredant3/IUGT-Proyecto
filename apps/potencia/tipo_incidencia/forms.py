from django import forms
from potencia.tipo_incidencia.models import TipoIncidencia
from helpers.FormBase import FormBase


class TipoIncidenciaForm(FormBase):
    class Meta:
        model = TipoIncidencia
        fields = ["tipo"]
        widgets = {
            "tipo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Fallo eléctrico"}
            ),
        }
