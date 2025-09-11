from administracion.departamentos.models import Departamento
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)
from administracion.tipo_averia.models import TipoAveria
from helpers.BaseModelMixin import BaseModel, DEP_AVERIA


class Averia(BaseModel):
    tipo_averia = ForeignKey(
        TipoAveria, on_delete=CASCADE, verbose_name="Tipo de avería"
    )
    departamento = ForeignKey(
        Departamento, on_delete=CASCADE, verbose_name="Departamento"
    )
    problema = TextField(
        "Problema",
        max_length=180,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )

    serial = CharField(
        "Serial",
        max_length=30,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(30),
            TextValidator(),
        ],
    )
    codigo_bn = CharField(
        "Código BN",
        max_length=30,
        validators=[MinLengthValidator(6), MaxLengthValidator(30), TextValidator()],
    )
    observaciones = TextField(
        "Observaciones",
        max_length=180,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
        null=True,
    )
    d_averia = CharField(
        "Depertamento que reporta Averia",
        max_length=13,
        choices=DEP_AVERIA,
    )

    class Meta:
        permissions = [
            ("listar_averia", "Puede listar averías"),
            ("agregar_averia", "Puede agregar avería"),
            ("ver_averia", "Puede ver avería"),
            ("editar_averia", "Puede editar avería"),
            ("eliminar_averia", "Puede eliminar avería"),
        ]
        db_table = "administracion_averia"
        verbose_name = "Avería"
        verbose_name_plural = "Averías"
        ordering = ["-created_at"]

    def __str__(self):
        return self.problema
