from django.forms import TextInput, Textarea, Select
from gestion_comunicacional.models import GestionComunicacional
from helpers.FormBase import FormBase

# from django import forms
# from helpers.models import BOOLEAN_CHOICES


class GestionComunicacionalForm(FormBase):
    # municipio_priorizado = forms.BooleanField(
    #     initial=False,
    #     required=False,
    #     widget=forms.CheckboxInput(
    #         attrs={"class": "form-check-input", "role": "switch", "value": "False"}
    #     ),
    #     choices=BOOLEAN_CHOICES,
    #     default=True,
    # )

    class Meta:
        model = GestionComunicacional
        fields = [
            "nombre_actividad",
            "actividad_realizada",
            "descripcion_actividad",
            "actividad_preventiva",
            "estado",
            "municipio",
            "parroquia",
            "estrategias_metodologicas",
            "ambito_accion",
            "poblacion_abordada",
            "municipio_priorizado",
            "equipo_social",
            "cedula",
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
            "nombre_actividad": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejem. vuelvan caras",
                }
            ),
            "descripcion_actividad": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción de la actividad",
                }
            ),
            "poblacion_abordada": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "nombre de la población abordada",
                }
            ),
            "actividad_realizada": Textarea(
                attrs={
                    "placeholder": "Ejem. MICRO-CONVERSATORIO",
                }
            ),
            "observaciones": Textarea(
                attrs={
                    "placeholder": "Ingrese las observaciones",
                }
            ),
            "estado": Select(attrs={"class": "form-select mb-3"}),
            "municipio": Select(attrs={"class": "form-select mb-3"}),
            "parroquia": Select(attrs={"class": "form-select mb-3"}),
            "cedula": TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 12345678"}
            ),
        }
