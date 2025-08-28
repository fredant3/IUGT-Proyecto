from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("rem", "En remodelación"),
    ("cer", "Cerrado"),
)


class Sede(BaseModel):
    sede = CharField(
        "Sede",
        max_length=30,
        validators=[MinLengthValidator(6), MaxLengthValidator(30), TextValidator()],
    )
    estatus = CharField("Estatus", max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.sede

    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
        permissions = [
            ("listar_sede", "Puede listar sedes"),
            ("agregar_sede", "Puede agregar sede"),
            ("ver_sede", "Puede ver sede"),
            ("editar_sede", "Puede actualizar sede"),
            ("eliminar_sede", "Puede eliminar sede"),
        ]
