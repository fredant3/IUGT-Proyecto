from helpers.RepositoryMixin import Repository

from presupuesto.cedente.models import Cedente


class CedenteRepository(Repository):
    def __init__(self):
        self.entity = Cedente
