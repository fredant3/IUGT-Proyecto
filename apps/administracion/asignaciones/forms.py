from administracion.asignaciones.models import Asignacion
from django.forms import TextInput, NumberInput
from helpers.FormBase import FormBase


class AsignacionForm(FormBase):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "cantidad": NumberInput(
                attrs={
                    "placeholder": "Ingrese la cantidad (número entero positivo)",
                    "step": "1",
                    "min": "1",
                }
            ),
            "descripcion": TextInput(
                attrs={"placeholder": "Ingrese una descripción (mínimo 10 caracteres)"}
            ),
            "observaciones": TextInput(
                attrs={"placeholder": "Ingrese observaciones (mínimo 10 caracteres)"}
            ),
        }


class AsignacionUpdateForm(FormBase):
    class Meta:
        model = Asignacion
        fields = [
            "articulo",
            "sede",
            "departamento",
            "cantidad",
            "descripcion",
            "observaciones",
        ]
        labels = {
            "articulo": "Artículo (solo lectura)",
            "sede": "Sede",
            "departamento": "Departamento",
            "cantidad": "Cantidad",
            "descripcion": "Descripción",
            "observaciones": "Observaciones",
        }
        widgets = {
            "cantidad": NumberInput(
                attrs={
                    "placeholder": "Ingrese la cantidad (número entero positivo)",
                    "step": "1",
                    "min": "1",
                }
            ),
            "descripcion": TextInput(
                attrs={"placeholder": "Ingrese una descripción (mínimo 10 caracteres)"}
            ),
            "observaciones": TextInput(
                attrs={"placeholder": "Ingrese observaciones (mínimo 10 caracteres)"}
            ),
        }
