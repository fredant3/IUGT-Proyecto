from helpers.RepositoryMixin import Repository

from .models import Actividad


class ActividadRepository(Repository):
    def __init__(self):
        self.entity = Actividad
