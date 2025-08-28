from django import forms
from planificacion.actividades.models import Actividad
from helpers.FormBase import FormBase


class ActividadForm(FormBase):
    fechai = FormBase.create_date_field("date", title="Fecha de inicio")
    fechaf = FormBase.create_date_field("date", title="Fecha de fin")

    class Meta:
        model = Actividad
        fields = (
            "fechai",
            "fechaf",
            "objetiv",
            "meta",
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
        labels = {"objetiv": "Objetivo", "meta": "Meta"}
        widgets = {
            "objetiv": forms.TextInput(
                attrs={
                    "placeholder": "Objetivo de la actividad",
                }
            ),
            "meta": forms.TextInput(
                attrs={
                    "placeholder": "Meta de la actividad",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        fechai = cleaned_data.get("fechai")
        fechaf = cleaned_data.get("fechaf")

        if fechai and fechaf and fechaf < fechai:
            raise forms.ValidationError(
                "La fecha de fin no puede ser anterior a la fecha de inicio."
            )

        return cleaned_data
