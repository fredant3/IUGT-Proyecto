from helpers.RepositoryMixin import Repository

from presupuesto.partida.models import Partida


class PartidaRepository(Repository):
    def __init__(self):
        self.entity = Partida
