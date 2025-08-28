from django.db.models import CharField
from helpers.BaseModelMixin import BaseModel
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
)
from helpers.validForm import TextValidator


class TipoAveria(BaseModel):
    nombre = CharField(
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200), TextValidator()],
    )

    class Meta:
        permissions = [
            ("listar_tipo_averia", "Puede listar tipos de averías"),
            ("agregar_tipo_averia", "Puede agregar tipo de avería"),
            ("ver_tipo_averia", "Puede ver tipo de avería"),
            ("editar_tipo_averia", "Puede editar tipo de avería"),
            ("eliminar_tipo_averia", "Puede eliminar tipo de avería"),
        ]

    def __str__(self):
        return self.nombre
