from helpers.CrudMixin import CrudService
from organizacion.normativas.repositories import NormativaRepository
from organizacion.reglamentos.repositories import ReglamentoRepository
from django.conf import settings


class OrganizacionService(CrudService):
    def __init__(self):
        self.normativaRepository = NormativaRepository()
        self.reglamentoRepository = ReglamentoRepository()

    def getLastThreeNormativas(self, select, orderBy, orderAsc):
        data = self.normativaRepository.getAll(select, orderBy, orderAsc)[:3]

        for field in data:
            if "file" in field:
                url_file = f"{settings.MEDIA_URL}{field['file']}"
                field["file"] = (
                    f'<img src="{url_file}" style="height:50px;width:50px;" />'
                )

        return data

    def getLastThreeReglamentos(self, select, orderBy, orderAsc):
        data = self.reglamentoRepository.getAll(select, orderBy, orderAsc)[:3]

        for field in data:
            if "file" in field:
                url_file = f"{settings.MEDIA_URL}{field['file']}"
                field["file"] = (
                    f'<img src="{url_file}" style="height:50px;width:50px;" />'
                )

        return data

    def getAll(
        self,
        draw,
        start,
        length,
        search=None,
        orderBy="created_at",
        orderAsc="asc",
        select=("name", "file", "date", "estado"),
        arg=None,
    ):
        normativas = self.getLastThreeNormativas(select, orderBy, orderAsc)
        reglamentos = self.getLastThreeReglamentos(select, orderBy, orderAsc)
        return self.response(list(normativas) + list(reglamentos), start, length, draw)

    def response(self, entities, start, length, draw):
        response = {}
        records_total = len(entities)
        response["draw"] = draw
        response["entities"] = entities
        response["recordsTotal"] = records_total
        response["recordsFiltered"] = records_total
        return response
