import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from organizacion.reglamentos.services import ReglamentoService
from organizacion.reglamentos.models import ESTATUS_CHOICES, PROGRESS_CHOICES


class ReglamentoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "organizacion.reglamentos.ver_reglamento"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organización"
        context["submodule"] = "Reglamentos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("reglamentos:create")
        context["listApiUrl"] = reverse_lazy("api_reglamentos:list")
        context["updateUrl"] = reverse_lazy("reglamentos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("reglamentos:delete", args=[0])
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
                "title": "Nombre de Reglamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "date",
                "name": "date",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "progre",
                "name": "progre",
                "title": "Progreso",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "estado",
                "name": "estado",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ReglamentoListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "organizacion.reglamentos.ver_reglamento"
    field_mappings = {"estado": ESTATUS_CHOICES, "progre": PROGRESS_CHOICES}

    def __init__(self):
        self.service = ReglamentoService()

    def _map_fields(self, data):
        # First handle the choice field mappings via the mixin
        data = super()._map_fields(data)

        if "entities" in data:
            for item in data["entities"]:
                # Handle date formatting (both string and datetime objects)
                if "date" in item and item["date"]:
                    if isinstance(item["date"], str):
                        item["date"] = item["date"][:10]
                    else:
                        # Assuming it's a datetime object if not string
                        item["date"] = item["date"].strftime("%Y-%m-%d")
        return data
