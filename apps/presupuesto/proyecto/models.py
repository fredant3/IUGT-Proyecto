from django.db.models import CharField, DateField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import UnicodeAlphaSpaceValidator, TextValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Proyecto(BaseModel):
    nombrep = CharField(
        "Nombre del Proyecto",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    fechai = DateField("Fecha de Inicio")
    fechac = DateField("Fecha de Culminación")
    situacionp = CharField(
        "Situación Presupuestaria",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    montoproyecto = CharField("Monto Total del Proyecto", max_length=64)
    responsableg = CharField(
        "Responsable Gerente",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    responsablet = CharField(
        "Responsable Técnico",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    responsabler = CharField(
        "Responsable Registrador",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    responsablea = CharField(
        "Responsable Administrativo",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    estatus = CharField(
        "Estatus del Proyecto",
        max_length=64,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombrep

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        permissions = [
            ("listar_proyecto", "Puede listar proyectos"),
            ("agregar_proyecto", "Puede agregar proyecto"),
            ("ver_proyecto", "Puede ver proyecto"),
            ("editar_proyecto", "Puede actualizar proyecto"),
            ("eliminar_proyecto", "Puede eliminar proyecto"),
            ("pdf_proyecto", "Puede generar pdf de proyecto"),
        ]
