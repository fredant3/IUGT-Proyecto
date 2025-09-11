from administracion.departamentos.models import Departamento
from helpers.RepositoryMixin import Repository


class DepartamentoRepository(Repository):
    def __init__(self):
        self.entity = Departamento
