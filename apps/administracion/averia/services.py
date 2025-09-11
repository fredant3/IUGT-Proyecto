from administracion.averia.repositories import AveriaRepository
from administracion.tipo_averia.repositories import TipoAveriaRepository
from administracion.departamentos.repositories import DepartamentoRepository
from helpers.CrudMixin import CrudService
from django.db.models import Q


class AveriaService(CrudService):
    select = (
        "id",
        "problema",
        "tipo_averia__nombre",
        "departamento__nombre",
        "serial",
        "codigo_bn",
        "d_averia",
    )

    def __init__(self):
        self.repository = AveriaRepository()
        self.tipo_averia_repository = TipoAveriaRepository()
        self.departamento_repository = DepartamentoRepository()

    def buscar_tipo_averia(self, tipo_averia_id):
        return self.tipo_averia_repository.getById(tipo_averia_id)

    def buscar_departamento(self, departamento_id):
        return self.departamento_repository.getById(departamento_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["tipo_averia"] = self.buscar_tipo_averia(payload.get("tipo_averia"))
        payload["departamento"] = self.buscar_departamento(payload.get("departamento"))
        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(departamento__nombre__icontains=search)
                | Q(problema__icontains=search)
                | Q(ubicacion__icontains=search)
            )

        return query
