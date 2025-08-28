from helpers.RepositoryMixin import Repository

from rrhh.familiares.models import Familiar


class FamiliarRepository(Repository):
    def __init__(self):
        self.entity = Familiar
