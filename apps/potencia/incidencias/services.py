from django.db.models import Q
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.sedes.repositories import SedeRepository
from helpers.CrudMixin import CrudService
from potencia.incidencias.repositories import (
    IncidenciaRepository,
    TipoIncidenciaRepository,
)


class IncidenciaService(CrudService):
    select = (
        "id",
        "estado",
        "tipo_solicitud",
        "sede__sede",
        "departamento__nombre",
        "tipo_incidencia__tipo",
        "observaciones",
    )

    def __init__(self):
        self.repository = IncidenciaRepository()
        self.repositorySede = SedeRepository()
        self.repositoryDepartamento = DepartamentoRepository()
        self.repositoryTipoIncidencia = TipoIncidenciaRepository()

    # BEGIN Create
    def search_sede(self, id):
        return self.repositorySede.getById(id)

    def search_departamento(self, id):
        return self.repositoryDepartamento.getById(id)

    def search_tipo_incidencia(self, id):
        return self.repositoryTipoIncidencia.getById(id)

    def relationship(self, payload, *arg, **kwargs):
        payload["sede"] = self.search_sede(payload["sede"])
        payload["departamento"] = self.search_departamento(payload["departamento"])
        payload["tipo_incidencia"] = self.search_tipo_incidencia(
            payload["tipo_incidencia"]
        )
        return payload

    # END Create

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(sede__sede__icontains=search)
                | Q(departamento__nombre__icontains=search)
                | Q(tipo_incidencia__tipo__icontains=search)
                | Q(estado__icontains=search)
                | Q(tipo_solicitud__icontains=search)
                | Q(observaciones__icontains=search)
            )

        return query

    def list(self, search=None, page=None, per_page=None, arg=None):
        query = self.criteria(search, arg)
        return self.repository.list(query, self.select, page, per_page)
