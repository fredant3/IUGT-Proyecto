from django.db.models import Q
from helpers.CrudMixin import CrudService
from .repositories import TipoIncidenciaRepository

class TipoIncidenciaService(CrudService):
    def __init__(self):
        self.repository = TipoIncidenciaRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(nombre_incidencia__icontains=search)
        return query