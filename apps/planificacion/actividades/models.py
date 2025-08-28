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


class Actividad(BaseModel):
    fechai = DateField(verbose_name="Fecha de Inicio")
    fechaf = DateField(verbose_name="Fecha Final")
    objetiv = CharField(
        max_length=64,
        verbose_name="Objetivos:",
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    meta = CharField(max_length=64, verbose_name="Meta:", default="")

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        permissions = [
            ("listar_actividad", "Puede listar actividades"),
            ("agregar_actividad", "Puede agregar actividad"),
            ("ver_actividad", "Puede ver actividad"),
            ("editar_actividad", "Puede actualizar actividad"),
            ("eliminar_actividad", "Puede eliminar actividad"),
        ]
