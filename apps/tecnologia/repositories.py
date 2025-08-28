from helpers.RepositoryMixin import Repository
from administracion.inventario.models import Articulo


class TecnologiaRepository(Repository):
    def __init__(self):
        self.entity = Articulo
