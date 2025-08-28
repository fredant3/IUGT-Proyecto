import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from administracion.sedes.services import SedeService
from administracion.sedes.models import ESTATUS_CHOICES


class SedeListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.sedes.listar_sede"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Sedes"
        context["createBtn"] = "Agregar sede"
        context["createUrl"] = reverse_lazy("sedes:create")
        context["listApiUrl"] = reverse_lazy("api_sedes:list")
        context["updateUrl"] = reverse_lazy("sedes:update", args=[0])
        context["deleteUrl"] = reverse_lazy("sedes:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("sedes:export_excel")
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
                "data": "sede",
                "name": "sede",
                "title": "Sede",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class SedeListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "administracion.sedes.listar_sede"
    field_mappings = {"estatus": ESTATUS_CHOICES}

    def __init__(self):
        self.service = SedeService()
