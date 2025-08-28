import json
from administracion.tipo_averia.services import TipoAveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout


class TipoAveriaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.tipo_averia.listar_tipo_averia"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "titlePage": "Administración",
                "indexUrl": reverse_lazy("administracion"),
                "module": "Administración",
                "submodule": "Tipos de Averías",
                "createBtn": "Nuevo tipo",
                "createUrl": reverse_lazy("tipo_averias:create"),
                "listApiUrl": reverse_lazy("api_tipo_averias:list"),
                "updateUrl": reverse_lazy("tipo_averias:update", args=[0]),
                "deleteUrl": reverse_lazy("tipo_averias:delete", args=[0]),
                "exportExcelUrl": reverse_lazy("tipo_averias:export_excel"),
                "heads": self.getColumns(),
                "columns": mark_safe(json.dumps(self.getColumns())),
            }
        )
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "ID",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "created_at",
                "name": "created_at",
                "title": "Fecha de creación",
                "orderable": "true",
                "searchable": "false",
            },
        ]


class TipoAveriaListApiView(ListController, CheckPermisosMixin):
    permission_required = "administracion.tipo_averia.listar_tipo_averia"

    def __init__(self):
        self.service = TipoAveriaService()
