from django.db.models import CharField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import UnicodeAlphaSpaceValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class Cargo(BaseModel):
    cargo = CharField(
        "Nombre del Cargo",
        max_length=60,
        unique=True,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(60),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    estatus = CharField("Estado del Cargo", max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        permissions = [
            ("listar_cargo", "Puede listar cargos"),
            ("agregar_cargo", "Puede agregar cargo"),
            ("ver_cargo", "Puede ver cargo"),
            ("editar_cargo", "Puede actualizar cargo"),
            ("eliminar_cargo", "Puede eliminar cargo"),
            ("exel_cargo", "Puede exportar cargo a excel"),
        ]
