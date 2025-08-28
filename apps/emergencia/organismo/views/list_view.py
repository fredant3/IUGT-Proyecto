import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from ..services import OrganismoService


class OrganismoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "operaciones.ver_emergencia"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipos de Organismo"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipos de Organismo"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("organismo:create")
        context["listApiUrl"] = reverse_lazy("api_organismo:list")
        context["updateUrl"] = reverse_lazy("organismo:update", args=[0])
        context["deleteUrl"] = reverse_lazy("organismo:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("organismo:export_excel")
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {"data": "id", "title": "ID"},
            {"data": "nombre", "title": "Organismo Competente"},
        ]


class OrganismoListApiView(ListController, CheckPermisosMixin):
    permission_required = "emergrncia.ver_emergencia"

    def __init__(self):
        self.service = OrganismoService()
