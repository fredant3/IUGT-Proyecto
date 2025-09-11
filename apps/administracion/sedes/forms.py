from helpers.FormBase import FormBase
from administracion.sedes.models import Sede
from django.forms import TextInput


class SedeForm(FormBase):
    class Meta:
        model = Sede
        fields = (
            "sede",
            "estatus",
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
            "sede": "Sede",
            "estatus": "Estatus",
        }
        widgets = {
            "sede": TextInput(attrs={"placeholder": "Ingrese el nombre de la sede"}),
        }
