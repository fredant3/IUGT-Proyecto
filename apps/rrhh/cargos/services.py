from helpers.CrudMixin import CrudService
from rrhh.cargos.repositories import CargoRepository
from django.db.models import Q

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("ina", "Inactivo"),
    ("inv", "Invalido"),
    ("cer", "Cerrado"),
)


class CargoService(CrudService):
    def __init__(self):
        self.repository = CargoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            estatus_codes = [
                code
                for code, name in ESTATUS_CHOICES
                if search.lower() in name.lower() or search.lower() == code.lower()
            ]

            query &= (
                Q(cargo__icontains=search)
                | Q(estatus__in=estatus_codes)
                | Q(estatus__icontains=search)
            )

        return query
