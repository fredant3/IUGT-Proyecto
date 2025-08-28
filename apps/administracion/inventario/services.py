from administracion.inventario.repositories import (
    ArticuloRepository,
    TipoArticuloRepository,
)
from helpers.CrudMixin import CrudService
from django.db.models import Q


class ArticuloService(CrudService):
    select = (
        "id",
        "tipo_articulo__nombre",
        "marca",
        "modelo",
        "fecha_adq",
        "codigo_bn",
        "serial",
    )

    def __init__(self):
        self.repository = ArticuloRepository()
        self.repositoryTypeArticle = TipoArticuloRepository()

    def search_type_article(self, tipo_articulo):
        search = self.repositoryTypeArticle.getEntity(("nombre", tipo_articulo))
        return search if search is not None else None

    def relationship(self, payload, *arg, **kwargs):
        payload["tipo_articulo"] = self.search_type_article(kwargs.get("type"))
        return payload

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(marca__icontains=search)
                | Q(modelo__icontains=search)
                | Q(serial__icontains=search)
                | Q(tipo_articulo__nombre__icontains=search)
            )
        return query
