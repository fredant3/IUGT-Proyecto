from django.db.models import Q
from helpers.CrudMixin import CrudService
from gestion_comunicacional.repositories import GestioncomunicacionalRepository

# from emergencia.incidencias.repositories import TipoIncidenciaRepository
# from emergencia.organismo.repositories import OrganismoRepository


class GestioncomunicacionalService(CrudService):

    def __init__(self):
        self.repository = GestioncomunicacionalRepository()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(nombre_actividad__icontains=search)
                | Q(descripcion_actividad__icontains=search)
                | Q(actividad_realizada__icontains=search)
            )

        return query
