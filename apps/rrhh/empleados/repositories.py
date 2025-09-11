from helpers.RepositoryMixin import Repository

from rrhh.empleados.models import Empleado


class EmpleadoRepository(Repository):
    def __init__(self):
        self.entity = Empleado
