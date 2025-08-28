from helpers.RepositoryMixin import Repository

from .models import Reglamento


class ReglamentoRepository(Repository):
    def __init__(self):
        self.entity = Reglamento
