from helpers.RepositoryMixin import Repository

from .models import Emergencia


class EmergenciaRepository(Repository):
    def __init__(self):
        self.entity = Emergencia
