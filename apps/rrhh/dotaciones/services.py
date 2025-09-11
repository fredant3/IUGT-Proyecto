from helpers.CrudMixin import CrudService
from rrhh.empleados.models import Empleado  # Importar modelo Empleado
from rrhh.empleados.repositories import EmpleadoRepository
from rrhh.dotaciones.repositories import DotacionRepository


class DotacionService(CrudService):
    select = (
        "id",
        "camisa",
        "pantalon",
        "zapato",
        "empleado__nombres",
    )

    def __init__(self):
        self.repository = DotacionRepository()
        self.empleado_repository = EmpleadoRepository()

    def buscar_empleado(self, empleado_id):
        return self.empleado_repository.getById(empleado_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.buscar_empleado(payload.get("empleado"))
        return payload
