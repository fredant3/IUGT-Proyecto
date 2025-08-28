import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.services import TipoSueldoService
from rrhh.tipos_sueldos.models import ESTATUS_CHOICES, TIPO_CHOICES


class TipoSueldoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Tipos de Sueldos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("tipos_sueldos:create")
        context["listApiUrl"] = reverse_lazy("api_tipos_sueldos:list")
        context["updateUrl"] = reverse_lazy("tipos_sueldos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("tipos_sueldos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_tipos_sueldos:export_excel")
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
                "data": "tipo",
                "name": "tipo",
                "title": "Tipo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "monto",
                "name": "monto",
                "title": "Monto",
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


class TipoSueldoListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_sueldos.listar_tipo_sueldo"
    field_mappings = {"estatus": ESTATUS_CHOICES, "tipo": TIPO_CHOICES}

    def __init__(self):
        self.service = TipoSueldoService()

    def _map_fields(self, data):
        # First handle the choice field mappings via the mixin
        data = super()._map_fields(data)

        if "entities" in data:
            for item in data["entities"]:
                # Additional field formatting can be added here if needed
                pass

        # Add filter options to response metadata
        if "meta" not in data:
            data["meta"] = {}

        data["meta"]["filters"] = {
            "tipo_options": self._choices_to_options(TIPO_CHOICES),
            "estatus_options": self._choices_to_options(ESTATUS_CHOICES),
        }

        return data

    def _choices_to_options(self, choices):
        """Convert Django choices to frontend options format"""
        return [{"value": k, "label": v} for k, v in choices]
