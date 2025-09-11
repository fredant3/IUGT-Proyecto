from helpers.RepositoryMixin import Repository

from .models import Sueldo


class SueldoRepository(Repository):
    def __init__(self):
        self.entity = Sueldo
