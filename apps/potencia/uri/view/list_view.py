import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from potencia.uri.services import UriService

from templates.sneat import TemplateLayout
from helpers.BaseModelMixin import ESTADOS_CHOICES


class UriListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "potencia.uri.listar_uri"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "URI"
        context["indexUrl"] = reverse_lazy("uri:list")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("uri:create")
        context["listApiUrl"] = reverse_lazy("api_uri:list")
        context["updateUrl"] = reverse_lazy("uri:update", args=[0])
        context["deleteUrl"] = reverse_lazy("uri:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_uri:export_excel")
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
                "data": "nroreporte",
                "name": "nroreporte",
                "title": "Nro. de Reporte",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "fecha_atencion",
                "name": "fecha_atencion",
                "title": "Fecha de Atencion",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "nombrepaciente",
                "name": "nombrepaciente",
                "title": "Nombres",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "apellidopaciente",
                "name": "apellidopaciente",
                "title": "Apellidos",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estado del Evento",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "via_reporte",
                "name": "via_reporte",
                "title": "Vía del Reporte",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class UriListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "potencia.uri.listar_uri"
    field_mappings = {"estado": ESTADOS_CHOICES}

    def __init__(self):
        self.service = UriService()
