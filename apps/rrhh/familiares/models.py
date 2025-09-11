from django.db.models import DateField, CharField, ForeignKey, CASCADE, BooleanField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import ESTADO_CIVIL_CHOICES, SEXO_CHOICES, BOOLEAN_CHOICES
from rrhh.empleados.models import Empleado
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import CharField, BooleanField
from helpers.validForm import (
    CedulaVenezolanaValidator,
    TextValidator,
    UnicodeAlphaSpaceValidator,
)

PARENTEZCO = (
    ("hermano", "Hermana|Hermano"),
    ("pareja", "Conyugue"),
    ("mama", "Madre"),
    ("papa", "Padre"),
    ("hijo", "Hija|Hijo"),
)
TIPO_HIJO = (
    ("menor_12", "Hijo menor de 12"),
    ("hijos_13_18", "Hijo entre 13 y 18"),
    ("mayor_18", "Hijo mayor de 18"),
)


class Familiar(BaseModel):
    parentezco = CharField(
        "Parentezco", max_length=7, choices=PARENTEZCO, blank=True, null=True
    )
    tipo_hijo = CharField(
        "Tipo de Hijo", max_length=11, choices=TIPO_HIJO, null=True, blank=True
    )
    discapacidad = BooleanField(
        "Discapacidad",
        choices=BOOLEAN_CHOICES,
        default=BOOLEAN_CHOICES[1],
        blank=True,
        null=True,
    )
    nombres = CharField(
        "Nombres del Familiar",
        max_length=90,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
        blank=True,
        null=True,
    )
    apellidos = CharField(
        "Apellidos del Familiar",
        max_length=90,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
        blank=True,
        null=True,
    )
    cedula = CharField(
        "Cédula de Identidad",
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
        blank=True,
        null=True,
    )
    fecha_nacimiento = DateField("Fecha de nacimiento", blank=True, null=True)
    sexo = CharField(
        "Género", max_length=1, choices=SEXO_CHOICES, blank=True, null=True
    )
    estado_civil = CharField(
        "Estado civil",
        max_length=1,
        choices=ESTADO_CIVIL_CHOICES,
        blank=True,
        null=True,
    )
    empleado = ForeignKey(
        Empleado, on_delete=CASCADE, verbose_name="Empleado", blank=True, null=True
    )
    observacion = CharField(
        "Observaciones",
        max_length=150,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(150),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "familiar"
        verbose_name_plural = "familiares"
        permissions = [
            ("listar_familiares", "Listar familiares"),
            ("agregar_familiar", "Agregar familiares"),
            ("ver_familiar", "Ver familiares"),
            ("modificar_familiar", "Modificar familiares"),
            ("eliminar_familiar", "Eliminar familiares"),
            ("exel_familiar", "Exportar familiares a excel"),
        ]
