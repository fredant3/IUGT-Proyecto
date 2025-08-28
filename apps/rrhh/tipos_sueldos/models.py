from django.db.models import CharField, TextField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import CurrencyValidator, TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

TIPO_CHOICES = (
    ("ticket", "Cesta Ticket"),
    ("guerra", "Bono de Guerra"),
    ("discapacidad", "Prima por discapacidad"),
    ("menor_12", "Prima por dependecias menores de 12"),
    ("hijos_13_18", "Prima por dependecias menores de 13 a 18"),
    ("hijos_discapacidad", "Prima por dependecias menores con discapacidad"),
    ("profesionalismo", "Prima por Profesionalismo"),
    ("minimo", "Sueldo Minimo"),
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("sup", "Suspendido"),
)


class TipoSueldo(BaseModel):
    tipo = CharField("Tipo de Sueldo", max_length=21, choices=TIPO_CHOICES)
    monto = TextField(
        "Monto Asignado",
        validators=[CurrencyValidator()],
    )
    descripcion = CharField(
        "Descripción Detallada",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(255), TextValidator()],
    )
    estatus = CharField("Estado Actual", max_length=3, choices=ESTATUS_CHOICES)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"
        permissions = [
            ("listar_tipo_sueldos", "Listar tipos de sueldos"),
            ("agregar_tipo_sueldo", "Agregar tipos de sueldos"),
            ("ver_tipo_sueldo", "Ver tipos de sueldos"),
            ("modificar_tipo_sueldo", "Modificar tipos de sueldos"),
            ("eliminar_tipo_sueldo", "Eliminar tipos de sueldos"),
            ("exel_tipo_sueldo", "Exportar tipos de sueldos a excel"),
        ]
