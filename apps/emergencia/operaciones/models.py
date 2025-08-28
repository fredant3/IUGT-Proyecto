from django.db.models import (
    CharField,
    TextField,
    ForeignKey,
    CASCADE,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES
from emergencia.incidencias.models import TipoIncidencia
from emergencia.organismo.models import Organismo
from helpers.validForm import (
    UnicodeAlphaSpaceValidator,
    TextValidator,
    PhoneNumberValidator,
)
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Emergencia(BaseModel):
    denunciante = CharField(
        "Nombre del denunciante",
        max_length=180,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(180),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    telefono_denunciante = CharField(
        "Teléfono del denunciante",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    estado = CharField("Estado", name="estado", max_length=2, choices=ESTADOS_CHOICES)
    municipio = CharField("Municipio", name="municipio", max_length=90)
    parroquia = CharField("Parroquia", name="parroquia", max_length=90)
    organismo = ForeignKey(Organismo, on_delete=CASCADE)
    incidencia = ForeignKey(TipoIncidencia, on_delete=CASCADE)
    direccion_incidencia = TextField(
        "Dirección de la incidencia",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    observaciones = TextField(
        "Observaciones",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(180), TextValidator()],
    )
    # Localizacion_sede soon
    telefono_cuadrante_paz = CharField(
        "Teléfono del Cuadrente de Paz",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.denunciante + " by-" + self.created_by

    class Meta:
        verbose_name = "emergencia"
        verbose_name_plural = "emergencias"
        permissions = [
            ("listar_emergencia", "Puede listar emergencias"),
            ("agregar_emergencia", "Puede agregar emergencia"),
            ("ver_emergencia", "Puede ver emergencia"),
            ("editar_emergencia", "Puede actualizar emergencia"),
            ("eliminar_emergencia", "Puede eliminar emergencia"),
        ]
