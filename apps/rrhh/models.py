from rrhh.cargos.models import Cargo
from rrhh.contratos.models import Contrato
from rrhh.dotaciones.models import Dotacion
from rrhh.educaciones.models import Educacion
from rrhh.empleados.models import Empleado
from rrhh.familiares.models import Familiar
from rrhh.sueldos.models import Sueldo
from rrhh.tipos_sueldos.models import TipoSueldo

__all__ = [
    "Cargo",
    "Empleado",
    "Contrato",
    "Educacion",
    "Dotacion",
    "Familiar",
    "TipoSueldo",
    "Sueldo",
]
