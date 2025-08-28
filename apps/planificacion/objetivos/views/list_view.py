import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import ObjetivoService


class ObjetivoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.objetivos.listar_objetivos"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Objetivos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("objetivos:create")
        context["listApiUrl"] = reverse_lazy("api_objetivos:list")
        context["updateUrl"] = reverse_lazy("objetivos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("objetivos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("objetivos:export_excel")
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
                "data": "fechai",
                "name": "fechai",
                "title": "Fecha inicial",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechaf",
                "name": "fechaf",
                "title": "Fecha final",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "objetiv",
                "name": "objetiv",
                "title": "Objetivo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "meta",
                "name": "meta",
                "title": "Meta",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class ObjetivoListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.objetivos.listar_objetivos"

    def __init__(self):
        self.service = ObjetivoService()
