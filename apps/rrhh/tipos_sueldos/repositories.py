from helpers.RepositoryMixin import Repository

from rrhh.tipos_sueldos.models import TipoSueldo


class TipoSueldoRepository(Repository):
    def __init__(self):
        self.entity = TipoSueldo
