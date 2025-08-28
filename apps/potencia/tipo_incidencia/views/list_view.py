import json

from potencia.tipo_incidencia.services import TipoIncidenciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class TipoIncidenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "potencia.tipoIncidencia.view_tipoIncidencia"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("potencia")
        context["module"] = "Potencia"
        context["submodule"] = "Tipos de Incidencias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("tipoIncidencia:create")
        context["listApiUrl"] = reverse_lazy("api_tipoIncidencia:list")
        context["updateUrl"] = reverse_lazy("tipoIncidencia:update", args=[0])
        context["deleteUrl"] = reverse_lazy("tipoIncidencia:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_tipoIncidencia:export_excel")
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
                "searchable": "false",
            },
            {
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class TipoIncidenciaListApiView(ListController, CheckPermisosMixin):
    permission_required = "potencia.tipoIncidencia.view_tipoIncidencia"

    def __init__(self):
        self.service = TipoIncidenciaService()
