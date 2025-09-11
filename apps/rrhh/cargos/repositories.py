from helpers.RepositoryMixin import Repository

from rrhh.cargos.models import Cargo


class CargoRepository(Repository):
    def __init__(self):
        self.entity = Cargo
