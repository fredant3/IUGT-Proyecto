from helpers.RepositoryMixin import Repository
from emergencia.incidencias.models import TipoIncidencia


class TipoIncidenciaRepository(Repository):
    def __init__(self):
        self.entity = TipoIncidencia
