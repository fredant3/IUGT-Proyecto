import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from presupuesto.cedente.services import CedenteService


class CedenteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.cedente.listar_cedente"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedentes"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("cedentes:create")
        context["listApiUrl"] = reverse_lazy("api_cedentes:list")
        context["updateUrl"] = reverse_lazy("cedentes:update", args=[0])
        context["deleteUrl"] = reverse_lazy("cedentes:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_cedentes:export_excel")
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
                "data": "idc",
                "name": "idc",
                "title": "Identificador",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "partidac",
                "name": "partidac",
                "title": "Partida",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "generalc",
                "name": "generalc",
                "title": "General",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "espefc",
                "name": "espefc",
                "title": "Específicaciones",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "subespefc",
                "name": "subespefc",
                "title": "Sub-Especialidad",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "denomc",
                "name": "denomc",
                "title": "Denomincación",
                "orderable": "false",
                "searchable": "false",
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
                "data": "direccionc",
                "name": "direccionc",
                "title": "Dirección cedente",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class CedenteListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.cedente.listar_cedente"

    def __init__(self):
        self.service = CedenteService()
