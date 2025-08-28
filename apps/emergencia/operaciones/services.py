from django.db.models import Q
from helpers.CrudMixin import CrudService
from .repositories import EmergenciaRepository
from emergencia.incidencias.repositories import TipoIncidenciaRepository
from emergencia.organismo.repositories import OrganismoRepository


class EmergenciaService(CrudService):
    select={
        "id",
        "denunciante",
        "telefono_denunciante",
        "incidencia__nombre_incidencia",
        "organismo__nombre",
        "created_by",
    }

    def __init__(self):
        self.repository = EmergenciaRepository()
        self.repositoryIncidence = TipoIncidenciaRepository()
        self.repositoryOrganismo = OrganismoRepository()

    def search_type_incidences(self, id):
        search = self.repositoryIncidence.getById(id)
        return search if search is not None else None

    def search_organismo(self, id):
        search = self.repositoryOrganismo.getById(id)
        return search if search is not None else None

    def relationship(self, payload, *arg, **kwargs):
        payload["incidencia"] = self.search_type_incidences(payload["incidencia"])
        payload["organismo"] = self.search_organismo(payload["organismo"])

        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(denunciante__icontains=search)
                | Q(incidencia__nombre_incidencia__icontains=search)
                | Q(organismo__nombre__icontains=search)
            )

        return query
