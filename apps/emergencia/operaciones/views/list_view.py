import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import EmergenciaService


class EmergenciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "operaciones.ver_emergencia"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Operaciones"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Operaciones"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("operaciones:create")
        context["listApiUrl"] = reverse_lazy("api_operaciones:list")
        context["updateUrl"] = reverse_lazy("operaciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("operaciones:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("operaciones:export_excel")
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
                "data": "denunciante",
                "name": "denunciante",
                "title": "Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "telefono_denunciante",
                "name": "telefono_denunciante",
                "title": "Telefono",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "incidencia__nombre_incidencia",
                "name": "incidencia__nombre_incidencia",
                "title": "Incidencia",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "organismo__nombre",
                "name": "organismo__nombre",
                "title": "Organismo Competente",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "created_by",
                "name": "created_by",
                "title": "Creado por",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class EmergenciaListApiView(ListController, CheckPermisosMixin):
    permission_required = "emergrncia.ver_emergencia"

    def __init__(self):
        self.service = EmergenciaService()
