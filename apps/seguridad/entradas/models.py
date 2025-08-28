from django.db.models import CharField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    CedulaVenezolanaValidator,
    UnicodeAlphaSpaceValidator,
    TextValidator,
    PhoneNumberValidator,
)
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Entrada(BaseModel):
    name = CharField(
        "Nombre",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellido = CharField(
        "Apellido",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    cedula = CharField(
        "Cédula",
        max_length=14,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    telefono = CharField(
        "Teléfono",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    fecha = DateField("Fecha")
    direccion = CharField(
        "Dirección",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    cargo = CharField("Cargo", max_length=64)
    hora = CharField("Hora de Entrada", max_length=64)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        permissions = [
            ("listar_entradas", "Listar entradas"),
            ("agregar_entrada", "Agregar entrada"),
            ("ver_entrada", "Ver entrada"),
            ("modificar_entrada", "Modificar entrada"),
            ("eliminar_entrada", "Eliminar entrada"),
        ]
