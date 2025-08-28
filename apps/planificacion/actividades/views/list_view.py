import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from ..services import ActividadService


class ActividadListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.actividades.ver_actividad"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Actividades"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("actividades:create")
        context["listApiUrl"] = reverse_lazy("api_actividades:list")
        context["updateUrl"] = reverse_lazy("actividades:update", args=[0])
        context["deleteUrl"] = reverse_lazy("actividades:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("actividades:export")
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
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fechaf",
                "name": "fechaf",
                "title": "Fecha",
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


class ActividadListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.actividades.ver_actividad"

    def __init__(self):
        self.service = ActividadService()
