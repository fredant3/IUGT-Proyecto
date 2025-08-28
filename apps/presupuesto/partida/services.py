from presupuesto.partida.repositories import PartidaRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class PartidaService(CrudService):
    def __init__(self):
        self.repository = PartidaRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(codigo__icontains=search) | Q(titulo__icontains=search)
        return query
