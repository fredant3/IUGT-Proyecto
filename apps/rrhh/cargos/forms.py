from django import forms
from rrhh.cargos.models import Cargo
from helpers.FormBase import FormBase


class CargoForm(FormBase):
    class Meta:
        model = Cargo
        fields = (
            "cargo",
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
        widgets = {
            "cargo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del Cargo"}
            ),
            "estatus": forms.Select(
                attrs={"class": "form-control", "placeholder": "Estado del Cargo"}
            ),
        }
