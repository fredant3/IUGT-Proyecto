from administracion.inventario.models import Articulo, TipoArticulo
from helpers.RepositoryMixin import Repository


class TipoArticuloRepository(Repository):
    def __init__(self):
        self.entity = TipoArticulo


class ArticuloRepository(Repository):
    def __init__(self):
        self.entity = Articulo
