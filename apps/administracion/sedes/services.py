from helpers.CrudMixin import CrudService

from .repositories import SedeRepository
from django.db.models import Q


class SedeService(CrudService):
    def __init__(self):
        self.repository = SedeRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(sede__icontains=search)

        return query
