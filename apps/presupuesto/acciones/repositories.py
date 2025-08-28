from helpers.RepositoryMixin import Repository

from presupuesto.acciones.models import Accion


class AccionRepository(Repository):
    def __init__(self):
        self.entity = Accion
