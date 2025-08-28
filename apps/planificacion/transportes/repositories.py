from helpers.RepositoryMixin import Repository

from .models import Transporte


class TransporteRepository(Repository):
    def __init__(self):
        self.entity = Transporte
