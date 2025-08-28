import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from tecnologia.services import TecnologiaService

from templates.sneat import TemplateLayout


class TecnologiaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología de la Informacion"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Inventario de Tecnología"
        context["listApiUrl"] = reverse_lazy("api_tecnologia:list")
        context["heads"] = columns
        context["updateUrl"] = reverse_lazy("tecnologia:update", args=[0])
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
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "descripcion",
                "name": "descripcion",
                "title": "Descripción",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "marca",
                "name": "marca",
                "title": "Marca",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "modelo",
                "name": "modelo",
                "title": "Modelo",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Serial",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "fecha_adq",
                "name": "fecha_adq",
                "title": "Adquirido",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class TecnologiaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = TecnologiaService()
