from django import forms
from presupuesto.receptor.models import Receptor
from helpers.FormBase import FormBase
from helpers.validForm import validate_decimal_number


class ReceptorForm(FormBase):
    caufechar = FormBase.create_date_field("caufechar", "Causado a la fecha")

    class Meta:
        model = Receptor
        fields = (
            "partida",
            "denomr",
            "presuacorr",
            "caufechar",
            "dispr",
            "montocr",
            "saldofr",
            "direccionr",
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
            "denomr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la denominación",
                }
            ),
            "presuacorr": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "dispr": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "montocr": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "saldofr": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "direccionr": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la dirección",
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
