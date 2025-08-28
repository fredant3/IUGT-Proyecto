from helpers.RepositoryMixin import Repository

from presupuesto.receptor.models import Receptor


class ReceptorRepository(Repository):
    def __init__(self):
        self.entity = Receptor
