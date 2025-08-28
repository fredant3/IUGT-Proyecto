from helpers.RepositoryMixin import Repository

from seguridad.salidas.models import Salida


class SalidaRepository(Repository):
    def __init__(self):
        self.entity = Salida
