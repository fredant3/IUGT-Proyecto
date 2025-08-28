from administracion.asignaciones.models import Asignacion
from helpers.RepositoryMixin import Repository


class AsignacionRepository(Repository):
    def __init__(self):
        self.entity = Asignacion
