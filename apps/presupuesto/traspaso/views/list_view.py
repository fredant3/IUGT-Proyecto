import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from presupuesto.cedente.services import CedenteService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class TraspasoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.traspaso.listar_traspaso"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("traspasos:create")
        context["listApiUrl"] = reverse_lazy("api_traspasos:list")
        context["updateUrl"] = reverse_lazy("traspasos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("traspasos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_traspasos:export_excel")
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
                "data": "partida__codigo",
                "name": "partida__codigo",
                "title": "Partida cedente Código",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "partida__titulo",
                "name": "partida__titulo",
                "title": "Partida cedente Título",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "presuacorc",
                "name": "presuacorc",
                "title": "Presupuesto acordado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "caufechac",
                "name": "caufechac",
                "title": "Causado a la fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "dispc",
                "name": "dispc",
                "title": "Disponible a causar",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "montocc",
                "name": "montocc",
                "title": "Monto a ceder",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "saldofc",
                "name": "saldofc",
                "title": "Saldo final",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "receptor__partida__codigo",
                "name": "receptor__partida__codigo",
                "title": "Receptor Partida Código",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "receptor__partida__titulo",
                "name": "receptor__partida__titulo",
                "title": "Receptor Partida Título",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "receptor__presuacorr",
                "name": "receptor__presuacorr",
                "title": "Presupuesto Receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "receptor__caufechar",
                "name": "receptor__caufechar",
                "title": "Causado Receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "receptor__dispr",
                "name": "receptor__dispr",
                "title": "Disponible Receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "receptor__montocr",
                "name": "receptor__montocr",
                "title": "Monto Receptor",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "receptor__saldofr",
                "name": "receptor__saldofr",
                "title": "Saldo Final Receptor",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class TraspasoListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.listar_traspaso"

    def __init__(self):
        self.service = CedenteService()
