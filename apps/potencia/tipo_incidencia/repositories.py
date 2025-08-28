from potencia.tipo_incidencia.models import TipoIncidencia
from helpers.RepositoryMixin import Repository


class TipoIncidencaRepository(Repository):
    def __init__(self):
        self.entity = TipoIncidencia
