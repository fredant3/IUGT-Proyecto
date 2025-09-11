from administracion.departamentos.models import Departamento
from administracion.inventario.models import Articulo
from administracion.sedes.models import Sede
from django.db.models import ForeignKey, IntegerField, TextField, CASCADE
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import PositiveIntegerValidator, TextValidator
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class Asignacion(BaseModel):
    LIST_ARTICLE = "administracion.listar_asignacion"
    ADD_ARTICLE = "administracion.agregar_asignacion"
    VIEW_ARTICLE = "administracion.ver_asignacion"
    CHANGE_ARTICLE = "administracion.editar_asignacion"
    DELETE_ARTICLE = "administracion.eliminar_asignacion"

    articulo = ForeignKey(Articulo, on_delete=CASCADE)
    sede = ForeignKey(Sede, on_delete=CASCADE)
    departamento = ForeignKey(Departamento, on_delete=CASCADE)
    cantidad = IntegerField(
        validators=[MinValueValidator(1), PositiveIntegerValidator()],
        help_text="La cantidad debe ser un número entero mayor o igual a 1.",
    )
    descripcion = TextField(
        max_length=255,
        validators=[MinLengthValidator(10), MaxLengthValidator(255), TextValidator()],
    )
    observaciones = TextField(
        max_length=255,
        validators=[MinLengthValidator(3), MaxLengthValidator(255), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "administracion_asignacion"
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
        ordering = ["-id"]
        permissions = [
            ("listar_asignacion", "Puede listar asignaciones"),
            ("agregar_asignacion", "Puede agregar asignacion"),
            ("ver_asignacion", "Puede ver asignacion"),
            ("editar_asignacion", "Puede actualizar asignacion"),
            ("eliminar_asignacion", "Puede eliminar asignacion"),
        ]
