from django.db.models import CharField, TextField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import (
    TIPO_ACTIVIDAD,
    DESARROLLO,
)

from helpers.validForm import TextValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class FrentePreventivo(BaseModel):
    donde_desarrollo = CharField(
        "Donde se Desarrolló", max_length=4, choices=DESARROLLO
    )
    personas_beneficiadas = TextField(
        "Personas beneficiadas",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    tipo_actividad = CharField(
        "Tipo de Actividad", max_length=3, choices=TIPO_ACTIVIDAD
    )
    fecha_realizo = DateField("Fecha de realización")
    observaciones = TextField(
        "Observaciones",
        max_length=180,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.donde_desarrollo + " by-" + self.created_by

    class Meta:
        verbose_name = "Frente Preventivo"
        verbose_name_plural = "Frentes Preventivos"
        permissions = [
            ("listar_frentepreventivo", "Puede listar frente preventivo"),
            ("agregar_frentepreventivo", "Puede agregar frente preventivo"),
            ("ver_frentepreventivo", "Puede ver frente preventivo"),
            (
                "editar_frentepreventivo",
                "Puede actualizar frente preventivo",
            ),
            (
                "eliminar_frentepreventivo",
                "Puede eliminar frente preventivo",
            ),
        ]
