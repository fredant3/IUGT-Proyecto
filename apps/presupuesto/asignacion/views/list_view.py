import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from presupuesto.asignacion.services import AsignacionService


class AsignacionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.asignacion.listar_asignacion"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Asignaciones"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("presupuesto_asignaciones:create")
        context["listApiUrl"] = reverse_lazy("api_presupuesto_asignaciones:list")
        context["updateUrl"] = reverse_lazy("presupuesto_asignaciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("presupuesto_asignaciones:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy(
            "presupuesto_asignaciones:export_excel"
        )
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
                "data": "departamento",
                "name": "departamento",
                "title": "Nombre de la dirección",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "presupuesto",
                "name": "presupuesto",
                "title": "Presupuesto asignado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "objetivo",
                "name": "objetivo",
                "title": "Objetivo general anual",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "partida__codigo",
                "name": "partida__codigo",
                "title": "Partida Código",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "partida__titulo",
                "name": "partida__titulo",
                "title": "Partida Título",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class AsignacionListApiView(ListController, CheckPermisosMixin):
    permission_required = "presupuesto.asignacion.listar_asignacion"

    def __init__(self):
        self.service = AsignacionService()
