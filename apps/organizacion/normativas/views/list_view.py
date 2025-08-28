import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from organizacion.normativas.services import NormativaService

from templates.sneat import TemplateLayout
from organizacion.normativas.models import ESTATUS_CHOICES, PROGRESS_CHOICES


class NormativaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "organizacion.normativas.ver_normativa"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organización"
        context["submodule"] = "Normativas"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("normativas:create")
        context["listApiUrl"] = reverse_lazy("api_normativas:list")
        context["updateUrl"] = reverse_lazy("normativas:update", args=[0])
        context["deleteUrl"] = reverse_lazy("normativas:delete", args=[0])
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
                "data": "name",
                "name": "name",
                "title": "Normativa",
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


class NormativaListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "organizacion.normativas.ver_normativa"
    field_mappings = {"estado": ESTATUS_CHOICES, "progre": PROGRESS_CHOICES}

    def __init__(self):
        self.service = NormativaService()

    def _map_fields(self, data):
        data = super()._map_fields(data)

        if "entities" in data:
            for item in data["entities"]:
                # Format date if present
                if "date" in item and item["date"]:
                    item["date"] = item["date"][:10]
        return data
