from administracion.asignaciones.repositories import AsignacionRepository
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.inventario.repositories import ArticuloRepository
from administracion.sedes.repositories import SedeRepository
from helpers.CrudMixin import CrudService
from django.db.models import Q


class AsignacionService(CrudService):
    select = (
        "id",
        "articulo__nombre",
        "sede__sede",
        "departamento__nombre",
        "cantidad",
        "descripcion",
        "observaciones",
        "created_by",
    )

    def __init__(self):
        self.repository = AsignacionRepository()
        self.repositoryArticle = ArticuloRepository()
        self.repositorySede = SedeRepository()
        self.repositoryDepartamento = DepartamentoRepository()

    def search_article(self, articuloId):
        return self.repositoryArticle.getById(articuloId)

    def search_sede(self, sedeId):
        return self.repositorySede.getById(sedeId)

    def search_departamento(self, departamentoId):
        return self.repositoryDepartamento.getById(departamentoId)

    def relationship(self, payload, *arg, **kwargs):
        payload["articulo"] = self.search_article(payload.get("articulo"))
        payload["sede"] = self.search_sede(payload.get("sede"))
        payload["departamento"] = self.search_departamento(payload.get("departamento"))

        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(sede__sede__icontains=search)
                | Q(articulo__serial__icontains=search)
                | Q(departamento__nombre__icontains=search)
                | Q(descripcion__icontains=search)
                | Q(observaciones__icontains=search)
            )

        return query

    def before_create(self, data):
        articulo_id = (
            data["articulo"].id if hasattr(data["articulo"], "id") else data["articulo"]
        )

        articulo = self.repositoryArticle.getById(articulo_id)

        try:
            cantidad_asignar = int(data["cantidad"])
        except (ValueError, TypeError):
            raise ValueError("La cantidad debe ser un número válido")

        if cantidad_asignar > articulo.cantidad:
            raise ValueError("No hay suficiente cantidad de este artículo")

        from django.db import transaction

        with transaction.atomic():
            articulo.cantidad -= cantidad_asignar
            articulo.save()
            data["articulo"] = articulo

        return data
