from helpers.CrudMixin import CrudService

from .repositories import ActividadRepository
from django.db.models import Q


class ActividadService(CrudService):
    def __init__(self):
        self.repository = ActividadRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(objetiv__icontains=search)
                | Q(meta__icontains=search)
                | Q(fechai__icontains=search)
                | Q(fechaf__icontains=search)
            )

        return query
