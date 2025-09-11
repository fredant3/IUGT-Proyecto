import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import ContratoService


class ContratoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.contratos.listar_contrato"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Contratos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("contratos:create")
        context["listApiUrl"] = reverse_lazy("api_contratos:list")
        context["updateUrl"] = reverse_lazy("contratos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("contratos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_contratos:export_excel")
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
                "data": "empleado__nombres",
                "name": "empleado__nombres",
                "title": "Empleado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "empleado__cedula",
                "name": "empleado__cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo de contrato",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cargo__cargo",
                "name": "cargo__cargo",
                "title": "Cargo",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ContratoListApiView(ListController, CheckPermisosMixin):
    permission_required = "rrhh.contratos.listar_contrato"

    def __init__(self):
        self.service = ContratoService()
