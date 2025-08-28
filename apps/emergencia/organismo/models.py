from django.db.models import CharField
from helpers.BaseModelMixin import BaseModel


class Organismo(BaseModel):
    nombre = CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("listar_organismo_emergencia", "Puede listar tipo organismo"),
            ("agregar_organismo_emergencia", "Puede agregar tipo organismo"),
            ("ver_organismo_emergencia", "Puede ver tipo organismo"),
            ("editar_organismo_emergencia", "Puede actualizar tipo organismo"),
            ("eliminar_organismo_emergencia", "Puede eliminar tipo organismo"),
        ]
