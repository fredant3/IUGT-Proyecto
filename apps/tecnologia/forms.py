from administracion.inventario.models import Articulo
from helpers.FormBase import FormBase


class TecnologiaForm(FormBase):
    class Meta:
        model = Articulo
        fields = ("descripcion", 
                    "modelo",
                    "serial",
                    "placa",
                    "cantidad_combustible",
                    "codigo_bn",
                    "cantidad",
                    "tipo_articulo",
                    "condicion",
                    "fecha_adq",
                    "asignado",
                  )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]

