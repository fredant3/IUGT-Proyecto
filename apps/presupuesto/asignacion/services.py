from presupuesto.partida.repositories import PartidaRepository
from helpers.CrudMixin import CrudService

from presupuesto.asignacion.repositories import AsignacionRepository
from django.db.models import Q


class AsignacionService(CrudService):
    select = (
        "id",
        "partida__codigo",
        "partida__titulo",
        "departamento",
        "presupuesto",
        "objetivo",
    )

    def __init__(self):
        self.repository = AsignacionRepository()
        self.partida_repo = PartidaRepository()

    def relationship(self, payload, *arg, **kwargs):
        """Método para procesar relaciones"""
        if "partida" in payload and payload["partida"]:
            payload["partida"] = self.partida_repo.getById(payload["partida"])
        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= Q(departamento__icontains=search) | Q(objetivo__icontains=search)

        return query
