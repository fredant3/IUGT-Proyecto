from django.db.models import CharField, DateField, ForeignKey, CASCADE
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado
from helpers.validForm import UnicodeAlphaSpaceValidator, TextValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Educacion(BaseModel):
    colegio = CharField(
        "Nombre del Colegio",
        max_length=120,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(120),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    codigo_titulo = CharField(
        "Código del Título",
        max_length=120,
        validators=[MinLengthValidator(4), MaxLengthValidator(120), TextValidator()],
    )
    titulo = CharField(
        "Titulo Obtenido",
        max_length=120,
        validators=[MinLengthValidator(4), MaxLengthValidator(120), TextValidator()],
    )
    area_conocimiento = CharField(
        "Área de Conocimiento",
        max_length=120,
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(120),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    fecha_inicio = DateField("Fecha de inicio")
    fecha_culminacion = DateField("Fecha de culminacion")
    enlace_certificado = CharField(
        "Enlace al Certificado",
        max_length=120,
        null=True,
        blank=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(120), TextValidator()],
    )
    empleado = ForeignKey(Empleado, on_delete=CASCADE, verbose_name="Empleado")

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = "educacion"
        verbose_name_plural = "educaciones"
        permissions = [
            ("listar_educacion", "Puede listar educacion"),
            ("agregar_educacion", "Puede agregar educacion"),
            ("ver_educacion", "Puede ver educacion"),
            ("editar_educacion", "Puede actualizar educacion"),
            ("eliminar_educacion", "Puede eliminar educacion"),
            ("exel_educacion", "Puede exportar educacion a excel"),
        ]
