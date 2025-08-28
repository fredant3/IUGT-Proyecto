from helpers.RepositoryMixin import Repository

from seguridad.vehiculos.models import Vehiculo


class VehiculoRepository(Repository):
    def __init__(self):
        self.entity = Vehiculo
