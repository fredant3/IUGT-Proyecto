from django.db.models import (
    CharField,
    TextField,
    DateField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("reg", "Registrado"),
    ("pro", "En Proceso"),
    ("nop", "No Procede"),
)


class RegistroFilmico(BaseModel):
    estatus = CharField(max_length=3, choices=ESTATUS_CHOICES)
    camara = CharField(
        "Cámara",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2), MaxLengthValidator(50), TextValidator()],
    )
    motivo_solicitud = TextField(
        "Motivo de Solicitud",
        max_length=400,
        validators=[MinLengthValidator(3), MaxLengthValidator(400), TextValidator()],
    )
    ente_solicita = CharField(
        "Ente que Solicita",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2), MaxLengthValidator(50), TextValidator()],
    )
    direccion = CharField(
        "Dirección",
        max_length=150,
        blank=True,
        null=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(150), TextValidator()],
    )
    fecha_solicitud = DateField(blank=True, null=True)
    fecha_culminacion = DateField(blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.camara

    class Meta:
        verbose_name = "Registro Filmico"
        verbose_name_plural = "Registros Filmicos"
        permissions = [
            ("listar_registro_filmico", "Puede listar registros filmicos"),
            ("agregar_registro_filmico", "Puede agregar registro filmico"),
            ("ver_registro_filmico", "Puede ver registro filmico"),
            ("editar_registro_filmico", "Puede actualizar registro filmico"),
            ("eliminar_registro_filmico", "Puede eliminar registro filmico"),
            ("exel_registro_filmico", "Puede exportar a exel registro filmico"),
        ]
