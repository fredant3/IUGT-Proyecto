from helpers.CrudMixin import CrudService

from rrhh.empleados.repositories import EmpleadoRepository
from django.db.models import Q


class EmpleadoService(CrudService):
    def __init__(self):
        self.repository = EmpleadoRepository()

    def criteria(self, search):
        query = Q()

        if search:
            query &= Q(cedula__icontains=search)
        return query
