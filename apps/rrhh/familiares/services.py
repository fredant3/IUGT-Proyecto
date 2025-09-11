from helpers.CrudMixin import CrudService
from rrhh.empleados.models import Empleado  # Importar modelo Empleado
from rrhh.empleados.repositories import EmpleadoRepository
from rrhh.familiares.repositories import FamiliarRepository


class FamiliarService(CrudService):
    select = (
        "id",
        "parentezco",
        "tipo_hijo",
        "discapacidad",
        "nombres",
        "apellidos",
        "cedula",
        "fecha_nacimiento",
        "sexo",
        "estado_civil",
        "empleado__nombres",
        "observacion",
    )

    def __init__(self):
        self.repository = FamiliarRepository()
        self.empleado_repository = EmpleadoRepository()

    def buscar_empleado(self, empleado_id):
        return self.empleado_repository.getById(empleado_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.buscar_empleado(payload.get("empleado"))
        return payload
