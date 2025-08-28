# forms.py
from django.forms import TextInput
from .models import TipoIncidencia
from helpers.FormBase import FormBase

class TipoIncidenciaForm(FormBase):
    class Meta:
        model = TipoIncidencia
        fields = ["nombre_incidencia"]
        widgets = {
            "nombre_incidencia": TextInput(attrs={"placeholder": "Ej. Incendio, Robo, etc."})
        }

        