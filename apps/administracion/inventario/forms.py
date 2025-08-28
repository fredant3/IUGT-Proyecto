from administracion.inventario.models import Articulo
from helpers.FormBase import FormBase
from django.forms import TextInput, NumberInput, IntegerField


class ArticuloForm(FormBase):
    fecha_adq = FormBase.create_date_field("fecha_adq", "Fecha Adquisición")

    class Meta:
        model = Articulo
        fields = [
            "nombre",
            "descripcion",
            "marca",
            "modelo",
            "serial",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]
        widgets = {
            "nombre": TextInput(
                attrs={"placeholder": "Ingrese el nombre del artículo"}
            ),
            "descripcion": TextInput(
                attrs={"placeholder": "Ingrese la descripción del artículo"}
            ),
            "marca": TextInput(attrs={"placeholder": "Ingrese la marca del artículo"}),
            "modelo": TextInput(
                attrs={"placeholder": "Ingrese el modelo del artículo"}
            ),
            "serial": TextInput(attrs={"placeholder": "Ingrese el número de serie"}),
            "codigo_bn": TextInput(
                attrs={"placeholder": "Ingrese el código de bienes nacionales"}
            ),
            "cantidad": NumberInput(
                attrs={"placeholder": "Ingrese la cantidad disponible", "min": 1}
            ),
        }


class TecnologiaForm(ArticuloForm):
    pass


class ConsumibleForm(ArticuloForm):
    pass


class MobiliarioForm(ArticuloForm):
    class Meta(ArticuloForm.Meta):
        fields = [
            "nombre",
            "descripcion",
            "serial",
            "codigo_bn",
            "cantidad",
            "condicion",
            "fecha_adq",
        ]


class VehiculoForm(ArticuloForm):
    placa = IntegerField(
        label="Placa",
        widget=TextInput(attrs={"placeholder": "Ingrese la placa del vehículo"}),
    )
    cantidad_combustible = IntegerField(
        label="Cantidad de combustible",
        widget=NumberInput(
            attrs={"placeholder": "Ingrese la cantidad de combustible", "min": 0}
        ),
    )

    class Meta(ArticuloForm.Meta):
        fields = ArticuloForm.Meta.fields + [
            "placa",
            "cantidad_combustible",
        ]
