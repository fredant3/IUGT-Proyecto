from administracion.tipo_averia.models import TipoAveria
from helpers.RepositoryMixin import Repository


class TipoAveriaRepository(Repository):
    def __init__(self):
        self.entity = TipoAveria

    def buscar_por_nombre(self, nombre):
        return self.entity.objects.filter(nombre__icontains=nombre)
