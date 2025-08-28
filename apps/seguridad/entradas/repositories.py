from helpers.RepositoryMixin import Repository

from seguridad.entradas.models import Entrada


class EntradaRepository(Repository):
    def __init__(self):
        self.entity = Entrada
