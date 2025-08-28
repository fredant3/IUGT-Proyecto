from helpers.CrudMixin import CrudService

from seguridad.gestiones.repositories import GestionRepository
from django.db.models import Q


class GestionService(CrudService):
    def __init__(self):
        self.repository = GestionRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:

            query &= (
                Q(name__icontains=search)
                | Q(apellido__icontains=search)
                | Q(cedula__icontains=search)
                | Q(tipo__icontains=search)
                | Q(descripcion__icontains=search)
                | Q(fecha__icontains=search)
                | Q(hora__icontains=search)
                | Q(cargo__icontains=search)
                | Q(direccion__icontains=search)
            )

        return query
