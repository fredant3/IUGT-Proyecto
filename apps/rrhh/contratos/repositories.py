from helpers.RepositoryMixin import Repository

from .models import Contrato


class ContratoRepository(Repository):
    def __init__(self):
        self.entity = Contrato
