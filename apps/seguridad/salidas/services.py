from helpers.CrudMixin import CrudService
from seguridad.salidas.repositories import SalidaRepository
from django.db.models import Q


class SalidaService(CrudService):
    def __init__(self):
        self.repository = SalidaRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(id__icontains=search)
                | Q(name__icontains=search)
                | Q(apellido__icontains=search)
                | Q(cedula__icontains=search)
                | Q(telefono__icontains=search)
                | Q(fecha__icontains=search)
                | Q(direccion__icontains=search)
                | Q(cargo__icontains=search)
                | Q(hora__icontains=search)
            )

        return query
