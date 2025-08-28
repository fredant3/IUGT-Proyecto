from django import forms
from presupuesto.cedente.models import Cedente
from helpers.FormBase import FormBase


class CedenteForm(FormBase):
    caufechac = FormBase.create_date_field("caufechac", "Causado a la fecha")

    class Meta:
        model = Cedente
        fields = (
            "partida",
            "denomc",
            "presuacorc",
            "caufechac",
            "dispc",
            "montocc",
            "saldofc",
            "direccionc",
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
            "denomc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: Proyecto de Infraestructura (mín. 4 caracteres)",
                    "maxlength": "255",
                }
            ),
            "presuacorc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "dispc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "montocc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "saldofc": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "direccionc": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ej: Av. Principal, Edificio Municipal",
                    "maxlength": "255",
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
