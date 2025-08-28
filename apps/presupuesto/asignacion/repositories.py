from helpers.RepositoryMixin import Repository

from presupuesto.asignacion.models import Asignacion


class AsignacionRepository(Repository):
    def __init__(self):
        self.entity = Asignacion
