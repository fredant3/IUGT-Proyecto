import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from seguridad.salidas.services import SalidaService


class SalidaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "seguridad.salidas.listar_salida"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Salidas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("salidas:create")
        context["listApiUrl"] = reverse_lazy("api_salidas:list")
        context["updateUrl"] = reverse_lazy("salidas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("salidas:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_salidas:export_excel")
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
                "data": "name",
                "name": "name",
                "title": "Nombre",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "apellido",
                "name": "apellido",
                "title": "Apellido",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "telefono",
                "name": "telefono",
                "title": "Teléfono",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "direccion",
                "name": "direccion",
                "title": "Dirección",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "hora",
                "name": "hora",
                "title": "Hora",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class SalidaListApiView(ListController, CheckPermisosMixin):
    permission_required = "seguridad.salidas.listar_salida"

    def __init__(self):
        self.service = SalidaService()
