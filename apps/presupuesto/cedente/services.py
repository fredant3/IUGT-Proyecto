import datetime
from presupuesto.receptor.repositories import ReceptorRepository
from helpers.CrudMixin import CrudService
from presupuesto.cedente.repositories import CedenteRepository
from presupuesto.receptor.models import Receptor
from django.db.models import Q


class CedenteService(CrudService):
    select = (
        "id",
        "partida__codigo",
        "partida__titulo",
        "presuacorc",
        "caufechac",
        "dispc",
        "montocc",
        "saldofc",
        "receptor__partida__codigo",
        "receptor__partida__titulo",
        "receptor__presuacorr",
        "receptor__caufechar",
        "receptor__dispr",
        "receptor__montocr",
        "receptor__saldofr",
    )

    def __init__(self):
        self.repository = CedenteRepository()
        self.repositoryReceptor = ReceptorRepository()

    def search_receptor(self, receptorId):
        return self.repositoryReceptor.getById(receptorId)

    def relationship(self, payload, *arg, **kwargs):
        payload["receptor"] = self.search_receptor(payload.get("receptor"))
        return payload

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(idc__icontains=search) | Q(espefc__icontains=search)
        return query

    def destroyer(self, payload):
        deleted_at = {
            "deleted_by": payload.deleted_by,
            "updated_by": payload.updated_by,
            "deleted_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }
        Receptor.objects.filter(cedente=payload).update(**deleted_at)
        return self.repository.delete(payload)
