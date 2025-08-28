from django.db.models import CharField, IntegerField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES, MONTH_CHOICES
from helpers.validForm import PositiveIntegerValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    MaxValueValidator,
)


class Transporte(BaseModel):
    estado = CharField(
        "Estado del transporte",
        name="estado",
        max_length=2,
        choices=ESTADOS_CHOICES,
    )
    mes = CharField("Mes de operación", max_length=3, choices=MONTH_CHOICES)
    transporte = CharField(
        "Tipo de transporte",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    cantidad = IntegerField(
        "Cantidad de unidades",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000),
            PositiveIntegerValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "transporte"
        verbose_name_plural = "transportes"
        permissions = [
            ("listar_transporte", "Puede listar transporte"),
            ("agregar_transporte", "Puede agregar transporte"),
            ("ver_transporte", "Puede ver transporte"),
            ("editar_transporte", "Puede actualizar transporte"),
            ("eliminar_transporte", "Puede eliminar transporte"),
        ]
