from helpers.RepositoryMixin import Repository

from rrhh.dotaciones.models import Dotacion


class DotacionRepository(Repository):
    def __init__(self):
        self.entity = Dotacion
