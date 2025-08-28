from helpers.CrudMixin import CrudService

from seguridad.entradas.repositories import EntradaRepository
from django.db.models import Q


class EntradaService(CrudService):
    def __init__(self):
        self.repository = EntradaRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(name__icontains=search)
                | Q(apellido__icontains=search)
                | Q(cedula__icontains=search)
                | Q(telefono__icontains=search)
                | Q(fecha__icontains=search)
                | Q(direccion__icontains=search)
                | Q(cargo__icontains=search)
                | Q(hora__icontains=search)
            )

        return query
