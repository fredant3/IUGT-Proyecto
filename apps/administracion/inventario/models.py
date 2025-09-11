from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    ForeignKey,
    CASCADE,
    DateField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel, YES_NO_CHOICES
from helpers.validForm import PositiveIntegerValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


TIPO_CONDICION = (
    ("N", "Nuevo"),
    ("U", "Usado"),
    ("D", "Deteriorado"),
    ("-", "No Aplica"),
)


class TipoArticulo(BaseModel):
    LIST_TYPE_ARTICLE = "listar_tipo_articulo"
    ADD_TYPE_ARTICLE = "agregar_tipo_articulo"
    VIEW_TYPE_ARTICLE = "ver_tipo_articulo"
    CHANGE_TYPE_ARTICLE = "editar_tipo_articulo"
    DELETE_TYPE_ARTICLE = "eliminar_tipo_articulo"

    nombre = CharField(max_length=180)

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_tipos_articulos"
        verbose_name = "Tipo de Articulo"
        verbose_name_plural = "Tipos de Articulos"
        ordering = ["-id"]
        permissions = [
            ("listar_tipo_articulo", "Puede listar tipos de articulos"),
            ("agregar_tipo_articulo", "Puede agregar tipo de articulo"),
            ("ver_tipo_articulo", "Puede ver tipo de articulo"),
            ("editar_tipo_articulo", "Puede actualizar tipo de articulo"),
            ("eliminar_tipo_articulo", "Puede eliminar tipo de articulo"),
        ]


class Articulo(BaseModel):
    LIST_ARTICLE = "listar_articulo"
    ADD_ARTICLE = "agregar_articulo"
    VIEW_ARTICLE = "ver_articulo"
    CHANGE_ARTICLE = "editar_articulo"
    DELETE_ARTICLE = "eliminar_articulo"

    nombre = TextField(
        "Nombre",
        max_length=150,
        validators=[MaxLengthValidator(150), TextValidator()],
    )
    descripcion = TextField(
        "Descripción",
        max_length=255,
        validators=[MinLengthValidator(5), MaxLengthValidator(255), TextValidator()],
    )
    marca = CharField(
        "Marca",
        max_length=120,
        validators=[MinLengthValidator(2), MaxLengthValidator(120), TextValidator()],
        blank=True,
        null=True,
    )
    modelo = CharField(
        "Modelo",
        max_length=120,
        validators=[MinLengthValidator(2), MaxLengthValidator(120), TextValidator()],
        blank=True,
        null=True,
    )
    serial = CharField(
        "Serial",
        max_length=30,
        blank=True,
        null=True,
        validators=[MinLengthValidator(7), MaxLengthValidator(30), TextValidator()],
    )
    placa = CharField(
        "Placa",
        max_length=10,
        blank=True,
        null=True,
        validators=[MinLengthValidator(7), MaxLengthValidator(10), TextValidator()],
    )
    cantidad_combustible = IntegerField(
        "Cantidad de combustible máx. (En litros)",
        blank=True,
        null=True,
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
    )
    codigo_bn = CharField(
        "Código BN",
        max_length=30,
        blank=True,
        null=True,
        validators=[MinLengthValidator(4), MaxLengthValidator(30), TextValidator()],
    )
    cantidad = IntegerField(
        "Cantidad",
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
        help_text="La cantidad debe ser un número entero positivo.",
    )
    tipo_articulo = ForeignKey(TipoArticulo, on_delete=CASCADE)
    condicion = CharField(
        "Condición",
        max_length=1,
        choices=TIPO_CONDICION,
        null=True,
        blank=True,
        default="-",
    )
    fecha_adq = DateField("Fecha de adquisición")
    asignado = CharField(max_length=8, choices=YES_NO_CHOICES, default="no")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_articulos"
        verbose_name = "Actividad social"
        verbose_name_plural = "Actividades sociales"
        ordering = ["-fecha_adq"]
        permissions = [
            ("listar_articulo", "Puede listar articulos"),
            ("agregar_articulo", "Puede agregar articulo"),
            ("ver_articulo", "Puede ver articulo"),
            ("editar_articulo", "Puede actualizar articulo"),
            ("eliminar_articulo", "Puede eliminar articulo"),
        ]
