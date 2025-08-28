from helpers.RepositoryMixin import Repository
from potencia.incidencias.models import Incidencia, TipoIncidencia


class TipoIncidenciaRepository(Repository):
    def __init__(self):
        self.entity = TipoIncidencia


class IncidenciaRepository(Repository):
    def __init__(self):
        self.entity = Incidencia
