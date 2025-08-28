from django.db.models import CharField
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class TipoIncidencia(BaseModel):
    tipo = CharField(
        "Tipo de Incidencia",
        max_length=120,
        validators=[MinLengthValidator(4), MaxLengthValidator(120), TextValidator()],
    )

    class Meta:
        permissions = [
            ("listar_tipo_incidencia", "Puede listar tipo incidencia"),
            ("agregar_tipo_incidencia", "Puede agregar tipo incidencia"),
            ("ver_tipo_incidencia", "Puede ver tipo incidencia"),
            ("editar_tipo_incidencia", "Puede actualizar tipo incidencia"),
            ("eliminar_tipo_incidencia", "Puede eliminar tipo incidencia"),
        ]

    def __str__(self):
        return self.tipo
