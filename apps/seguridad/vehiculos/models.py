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


class Vehiculo(BaseModel):
    nombre = CharField(
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
        "Cédula de identidad",
        max_length=14,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    modelo = CharField(
        "Modelo",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    vehiculo = CharField(
        "Tipo de vehiculo",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    motivo = CharField(
        "Motivo",
        max_length=64,
        validators=[MinLengthValidator(4), MaxLengthValidator(64), TextValidator()],
    )
    capagasolina = CharField("Capacidad de Gasolina", max_length=64)
    cantigasolina = CharField("Cantidad de Gasolina", max_length=64)
    placa = CharField("Placa", max_length=64)
    fecha = DateField("Fecha")
    hora = CharField("Hora", max_length=64)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
        permissions = [
            ("listar_vehiculos", "Listar vehiculos"),
            ("agregar_vehiculo", "Agregar vehiculo"),
            ("ver_vehiculo", "Ver vehiculo"),
            ("modificar_vehiculo", "Modificar vehiculo"),
            ("eliminar_vehiculo", "Eliminar vehiculo"),
        ]
