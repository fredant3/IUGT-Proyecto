from django.db.models import CharField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    CedulaVenezolanaValidator,
    UnicodeAlphaSpaceValidator,
    TextValidator,
)
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Gestion(BaseModel):
    name = CharField(
        "Nombre",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellido = CharField(
        "Apellido",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(255),
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
    tipo = CharField(
        "Tipo de Gestión",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    descripcion = CharField(
        "Descripción",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    fecha = DateField("Fecha")
    direccion = CharField(
        "Dirección",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    cargo = CharField(
        "Cargo",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    hora = CharField(
        "Hora de Entrada",
        max_length=64,
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.name, self.apellido)

    class Meta:
        verbose_name = "gestion"
        verbose_name_plural = "gestiones"
        permissions = [
            ("listar_gestiones", "Listar gestiones"),
            ("agregar_gestion", "Agregar gestion"),
            ("ver_gestion", "Ver gestion"),
            ("modificar_gestion", "Modificar gestion"),
            ("eliminar_gestion", "Eliminar gestion"),
        ]
