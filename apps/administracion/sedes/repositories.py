from helpers.RepositoryMixin import Repository

from .models import Sede


class SedeRepository(Repository):
    def __init__(self):
        self.entity = Sede
