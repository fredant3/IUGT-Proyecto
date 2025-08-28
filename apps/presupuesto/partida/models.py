from django.db.models import CharField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    PartidaCodeValidator,
    TextValidator,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Partida(BaseModel):
    codigo = CharField(
        "Código:",
        max_length=64,
        unique=True,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(64),
            PartidaCodeValidator(),
        ],
    )
    titulo = CharField(
        "Título:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"
        permissions = [
            ("listar_partida", "Puede listar partida"),
            ("agregar_partida", "Puede agregar partida"),
            ("ver_accion", "Puede ver partida"),
            ("editar_partida", "Puede actualizar partida"),
            ("eliminar_partida", "Puede eliminar partida"),
            ("pdf_partida", "Puede generar pdf de accion"),
        ]
