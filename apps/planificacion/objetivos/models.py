from django.db.models import (
    CharField,
    DateField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)


class Objetivo(BaseModel):
    fechai = DateField(verbose_name="Fecha de Inicio")
    fechaf = DateField(verbose_name="Fecha Final")
    objetiv = CharField(
        max_length=64,
        verbose_name="Objetivos:",
        validators=[MinLengthValidator(3), MaxLengthValidator(64), TextValidator()],
    )
    meta = CharField(max_length=64, verbose_name="Meta:", default="")

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "objetivo"
        verbose_name_plural = "objetivos"
        permissions = [
            ("listar_objetivo", "Puede listar objetivos"),
            ("agregar_objetivo", "Puede agregar objetivo"),
            ("ver_objetivo", "Puede ver objetivo"),
            ("editar_objetivo", "Puede actualizar objetivo"),
            ("eliminar_objetivo", "Puede eliminar objetivo"),
        ]
