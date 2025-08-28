from administracion.averia.models import Averia
from helpers.RepositoryMixin import Repository


class Reporte_AveriaRepository(Repository):
    def __init__(self):
        self.entity = Averia
