from django.db.models import CharField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    CurrencyValidator,
    TextValidator,
    UnicodeAlphaSpaceValidator,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator

PROYECTOS_ACCIONES = (
    ("proyecto", "Proyecto"),
    ("accion", "Acciones Centralizadas"),
)


class Accion(BaseModel):
    proyecto_acciones = CharField(
        "Proyecto o Acciones Centralizadas",
        max_length=64,
        choices=PROYECTOS_ACCIONES,
        null=True,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    fecha_inicio = DateField("Fecha de Inicio")
    fecha_culminacion = DateField("Fecha de Culminación")
    situacion_presupuestaria = CharField(
        "Situación Presupuestaria:",
        max_length=64,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    monto = CharField(
        "Monto asignado:",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    responsable_gerente = CharField(
        "Responsable Gerente:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_tecnico = CharField(
        "Responsable Técnico:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_registrador = CharField(
        "Responsable Registrador:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )
    responsable_administrativo = CharField(
        "Responsable Administrativo:",
        max_length=64,
        validators=[MinLengthValidator(6), MaxLengthValidator(64), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.proyecto_acciones

    class Meta:
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"
        permissions = [
            ("listar_accion", "Puede listar acciones"),
            ("agregar_accion", "Puede agregar accion"),
            ("ver_accion", "Puede ver accion"),
            ("editar_accion", "Puede actualizar accion"),
            ("eliminar_accion", "Puede eliminar accion"),
            ("pdf_accion", "Puede generar pdf de accion"),
        ]
