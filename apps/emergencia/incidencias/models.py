from django.db.models import CharField
from helpers.BaseModelMixin import BaseModel


class TipoIncidencia(BaseModel):
    nombre_incidencia = CharField(max_length=120)

    def __str__(self):
        return self.nombre_incidencia

    class Meta:
        permissions = [
            ("listar_tipo_incidencia_emergencia", "Puede listar tipo incidencia"),
            ("agregar_tipo_incidencia_emergencia", "Puede agregar tipo incidencia"),
            ("ver_tipo_incidencia_emergencia", "Puede ver tipo incidencia"),
            ("editar_tipo_incidencia_emergencia", "Puede actualizar tipo incidencia"),
            ("eliminar_tipo_incidencia_emergencia", "Puede eliminar tipo incidencia"),
        ]
