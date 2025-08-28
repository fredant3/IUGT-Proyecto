from django import forms
from planificacion.objetivos.models import Objetivo
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_decimal_number,
)


class ObjetivoForm(FormBase):
    fechai = FormBase.create_date_field("fechai", title="Fecha Inicio")
    fechaf = FormBase.create_date_field("fechaf", title="Fecha Fin")

    class Meta:
        model = Objetivo
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
        labels = {"objetiv": "Objetivo estratégico", "meta": "Meta cuantitativa"}
        widgets = {
            "objetiv": forms.Textarea(
                attrs={
                    "placeholder": "Escribe aquí el objetivo estratégico",
                }
            ),
            "meta": forms.NumberInput(
                attrs={
                    "placeholder": "Escribe aquí la meta cuantitativa",
                    "step": "0.01",
                    "min": "0",
                }
            ),
        }

    def clean_meta(self):
        meta = self.cleaned_data.get("meta")
        validate_decimal_number(
            str(meta), "La meta debe ser un número positivo (ej: 100 o 75.5)"
        )
        return meta

    def clean(self):
        cleaned_data = super().clean()
        fechai = cleaned_data.get("fechai")
        fechaf = cleaned_data.get("fechaf")

        if fechai and fechaf and fechaf < fechai:
            self.add_error(
                "fechaf", "La fecha de fin no puede ser anterior a la fecha de inicio"
            )

        return cleaned_data
