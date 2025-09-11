from administracion.asignaciones.models import Asignacion
from administracion.averia.models import Averia
from administracion.compras.model import Compra
from administracion.departamentos.models import Departamento
from administracion.inventario.models import Articulo, TipoArticulo
from administracion.sedes.models import Sede
from administracion.tipo_averia.models import TipoAveria

__all__ = [
    "Departamento",
    "Articulo",
    "TipoArticulo",
    "Sede",
    "Compra",
    "Averia",
    "TipoAveria",
    "Asignacion",
]
