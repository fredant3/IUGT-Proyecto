from helpers.RepositoryMixin import Repository

from .models import Objetivo


class ObjetivoRepository(Repository):
    def __init__(self):
        self.entity = Objetivo
