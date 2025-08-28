from helpers.RepositoryMixin import Repository

from presupuesto.proyecto.models import Proyecto


class ProyectoRepository(Repository):
    def __init__(self):
        self.entity = Proyecto
