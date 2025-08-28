from django.db.models import Q
from helpers.CrudMixin import CrudService
from tecnologia.repositories import TecnologiaRepository


class TecnologiaService(CrudService):
    def __init__(self):
        self.repository = TecnologiaRepository()

    def criteria(self, search):
        query = Q(tipo_articulo__nombre="tecnologia")

        if search:
            query &= Q(marca__icontains=search) | Q(modelo__icontains=search)

        return query

    def getAll(
        self, draw, start, length, search=None, orderBy=None, orderAsc=None, select=(""), columns=[],
    ):
        select = select if select else self.select
        search = self.criteria(search)
        entities = self.repository.getFilter(search, select, orderBy, orderAsc)

        return self.response(entities, start, length, draw)
