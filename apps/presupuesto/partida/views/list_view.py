import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from presupuesto.partida.services import PartidaService


class PartidaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.partida.listar_partida"
    url_redirect = reverse_lazy("partida")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Partida"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("partida:create")
        context["listApiUrl"] = reverse_lazy("api_partida:list")
        context["updateUrl"] = reverse_lazy("partida:update", args=[0])
        context["deleteUrl"] = reverse_lazy("partida:delete", args=[0])

        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "codigo",
                "name": "codigo",
                "title": "codigo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "titulo",
                "name": "titulo",
                "title": "Titulo",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class PartidaListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.partida.listar_partida"

    def __init__(self):
        self.service = PartidaService()
