from helpers.CrudMixin import CrudService

from presupuesto.receptor.repositories import ReceptorRepository
from django.db.models import Q


class ReceptorService(CrudService):
    def __init__(self):
        self.repository = ReceptorRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(partidar__icontains=search)
                | Q(espefr__icontains=search)
                | Q(direccionr__icontains=search)
            )

        return query
