import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from potencia.incidencias.services import IncidenciaService

from templates.sneat import TemplateLayout
from helpers.BaseModelMixin import ESTADOS_CHOICES


class IncidenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "potencia.incidencias.listar_incidencias"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("potencia")
        context["module"] = "Potencia"
        context["submodule"] = "Incidencias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("incidencias:create")
        context["listApiUrl"] = reverse_lazy("api_incidencias:list")
        context["updateUrl"] = reverse_lazy("incidencias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("incidencias:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("incidencias:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "#",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo_solicitud",
                "name": "tipo_solicitud",
                "title": "Tipo de Solicitud",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "sede__sede",
                "name": "sede__sede",
                "title": "Sede",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "departamento__nombre",
                "name": "departamento__nombre",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "tipo_incidencia__tipo",
                "name": "tipo_incidencia__tipo",
                "title": "Tipo de Incidencia",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class IncidenciaListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "potencia.incidencias.listar_incidencias"
    field_mappings = {"estado": ESTADOS_CHOICES}

    def __init__(self):
        self.service = IncidenciaService()
