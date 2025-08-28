from helpers.RepositoryMixin import Repository

from .models import Infraestructura


class InfraestructuraRepository(Repository):
    def __init__(self):
        self.entity = Infraestructura
