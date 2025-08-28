from django import forms
from potencia.incidencias.models import Incidencia


class IncidenciaForm(forms.ModelForm):
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
