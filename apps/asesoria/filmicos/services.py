from django.db.models import Q
from asesoria.filmicos.repositories import RegistroFilmicoRepository
from helpers.CrudMixin import CrudService


class RegistroFilmicoService(CrudService):
    def __init__(self):
        self.repository = RegistroFilmicoRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(ente_solicita__icontains=search)
                | Q(motivo_solicitud__icontains=search)
                | Q(estatus__icontains=search)
            )

        return query
