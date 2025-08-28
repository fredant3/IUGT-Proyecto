# services.py
from django.db.models import Q
from helpers.CrudMixin import CrudService
from .repositories import OrganismoRepository

class OrganismoService(CrudService):
    def __init__(self):
        self.repository = OrganismoRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(nombre__icontains=search)
        return query