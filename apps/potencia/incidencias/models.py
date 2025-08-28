from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db.models import CASCADE, CharField, ForeignKey
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, ESTADOS_CHOICES
from potencia.tipo_incidencia.models import TipoIncidencia
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

INCIDENCIA_CHOICES = (
    ("Interna", "Solicitud Interna"),
    ("Externa", "Solicitud Externa"),
)


class Incidencia(BaseModel):
    sede = ForeignKey(Sede, on_delete=CASCADE)
    departamento = ForeignKey(Departamento, on_delete=CASCADE)
    tipo_incidencia = ForeignKey(
        TipoIncidencia, on_delete=CASCADE, verbose_name="Tipo de incidencia"
    )
    estado = CharField("Estado", max_length=15, choices=ESTADOS_CHOICES)
    tipo_solicitud = CharField(
        "Tipo de Solicitud", max_length=10, choices=INCIDENCIA_CHOICES
    )
    observaciones = CharField(
        "Descripción de la falla",
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        permissions = [
            ("listar_incidencia", "Puede listar incidencia"),
            ("agregar_incidencia", "Puede agregar incidencia"),
            ("ver_incidencia", "Puede ver incidencia"),
            ("editar_incidencia", "Puede actualizar incidencia"),
            ("eliminar_incidencia", "Puede eliminar incidencia"),
        ]
