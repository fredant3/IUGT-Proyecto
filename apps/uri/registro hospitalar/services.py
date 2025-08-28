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
