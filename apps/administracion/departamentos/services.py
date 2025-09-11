from administracion.departamentos.repositories import DepartamentoRepository
from helpers.CrudMixin import CrudService
from django.db.models import Q


class DepartamentoService(CrudService):
    def __init__(self):
        self.repository = DepartamentoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(nombre__icontains=search)

        return query
