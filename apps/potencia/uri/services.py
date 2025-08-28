from helpers.CrudMixin import CrudService
from potencia.uri.repositories import UriRepository
from django.db.models import Q


class UriService(CrudService):

    select = {
        "id",
        "fecha_atencion",
        "nombrepaciente",
        "apellidopaciente",
        "estado",
        "nroreporte",
        "via_reporte",
    }

    def __init__(self):
        self.repository = UriRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(nroreporte__icontains=search)
                | Q(fecha_atencion__icontains=search)
                | Q(nombrepaciente__icontains=search)
                | Q(apellidopaciente__icontains=search)
                | Q(estado__icontains=search)
                | Q(via_reporte__icontains=search)
            )

        return query

    def list(self, search=None, page=None, per_page=None, arg=None):
        query = self.criteria(search, arg)
        return self.repository.list(query, self.select, page, per_page)
