from django.db.models import Q
from helpers.CrudMixin import CrudService
from .repositories import ObjetivoRepository


class ObjetivoService(CrudService):
    def __init__(self):
        self.repository = ObjetivoRepository()

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
