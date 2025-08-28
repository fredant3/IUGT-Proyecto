from django.forms import TextInput, Textarea, Select
from emergencia.operaciones.models import Emergencia
from helpers.FormBase import FormBase


class EmergenciaForm(FormBase):
    class Meta:
        model = Emergencia
        fields = [
            "denunciante",
            "telefono_denunciante",
            "estado",
            "municipio",
            "parroquia",
            "incidencia",
            "organismo",
            "direccion_incidencia",
            "telefono_cuadrante_paz",
            "observaciones",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "denunciante": TextInput(
                attrs={
                    "placeholder": "Ejem. George Harris",
                }
            ),
            "telefono_denunciante": TextInput(
                attrs={"placeholder": "Ejem. 04125248935"}
            ),
            "direccion_incidencia": Textarea(
                attrs={
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "telefono_cuadrante_paz": TextInput(
                attrs={"placeholder": "Ejem. 04125248935"}
            ),
            "observaciones": Textarea(
                attrs={
                    "placeholder": "Ingrese las observaciones",
                }
            ),
            "estado": Select(attrs={"class": "form-select mb-3"}),
            "municipio": Select(attrs={"class": "form-select mb-3"}),
            "parroquia": Select(attrs={"class": "form-select mb-3"}),
        }
