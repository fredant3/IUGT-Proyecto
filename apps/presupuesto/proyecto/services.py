from helpers.CrudMixin import CrudService

from presupuesto.proyecto.repositories import ProyectoRepository
from django.db.models import Q


class ProyectoService(CrudService):
    def __init__(self):
        self.repository = ProyectoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(nombrep__icontains=search) | Q(responsableg__icontains=search)

        return query
