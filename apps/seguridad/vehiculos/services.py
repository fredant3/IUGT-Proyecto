from helpers.CrudMixin import CrudService
from seguridad.vehiculos.repositories import VehiculoRepository
from django.db.models import Q


class VehiculoService(CrudService):
    def __init__(self):
        self.repository = VehiculoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(id__icontains=search)
                | Q(nombre__icontains=search)
                | Q(apellido__icontains=search)
                | Q(cedula__icontains=search)
                | Q(modelo__icontains=search)
                | Q(vehiculo__icontains=search)
                | Q(motivo__icontains=search)
                | Q(capagasolina__icontains=search)
                | Q(cantigasolina__icontains=search)
                | Q(placa__icontains=search)
                | Q(fecha__icontains=search)
                | Q(hora__icontains=search)
            )

        return query
