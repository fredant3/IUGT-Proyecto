from administracion.compras.model import Compra
from helpers.FormBase import FormBase
from django.forms import TextInput, NumberInput


class CompraForm(FormBase):
    class Meta:
        model = Compra
        fields = ["articulo", "n_orden", "valor_bs"]
        widgets = {
            "n_orden": NumberInput(
                attrs={
                    "placeholder": "Ingrese el número de orden",
                    "min": 1,
                }
            ),
            "valor_bs": TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
        }
