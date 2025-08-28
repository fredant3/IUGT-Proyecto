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


class Infraestructura(BaseModel):
    estado = CharField(
        "Estado de la infraestructura",
        name="estado",
        max_length=2,
        choices=ESTADOS_CHOICES,
    )
    mes = CharField("Mes programado", max_length=3, choices=MONTH_CHOICES)
    infraestructura = CharField(
        "Nombre de la infraestructura",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    cantidad = IntegerField(
        "Cantidad estimada",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000),
            PositiveIntegerValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "infraestructura"
        verbose_name_plural = "infraestructuras"
        permissions = [
            ("listar_infraestructura", "Puede listar infraestructura"),
            ("agregar_infraestructura", "Puede agregar infraestructura"),
            ("ver_infraestructura", "Puede ver infraestructura"),
            ("editar_infraestructura", "Puede actualizar infraestructura"),
            ("eliminar_infraestructura", "Puede eliminar infraestructura"),
        ]
