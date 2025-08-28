import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from presupuesto.receptor.services import ReceptorService


class ReceptorListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.receptor.listar_receptor"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptores"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("receptores:create")
        context["listApiUrl"] = reverse_lazy("api_receptores:list")
        context["updateUrl"] = reverse_lazy("receptores:update", args=[0])
        context["deleteUrl"] = reverse_lazy("receptores:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_receptores:export_excel")
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
                "data": "partidar",
                "name": "partidar",
                "title": "Partida",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "generalr",
                "name": "generalr",
                "title": "General",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "espefr",
                "name": "espefr",
                "title": "Específicaciones",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "subespefr",
                "name": "subespefr",
                "title": "Sub-Especialidad",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "denomr",
                "name": "denomr",
                "title": "Denomincación",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "presuacorr",
                "name": "presuacorr",
                "title": "Presupuesto acordado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "caufechar",
                "name": "caufechar",
                "title": "Causado a la fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "dispr",
                "name": "dispr",
                "title": "Disponible a causar",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "montocr",
                "name": "montocr",
                "title": "Monto a ceder",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "saldofr",
                "name": "saldofr",
                "title": "Saldo final",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "direccionr",
                "name": "direccionr",
                "title": "Dirección cedente",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ReceptorListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.receptor.listar_receptor"

    def __init__(self):
        self.service = ReceptorService()
