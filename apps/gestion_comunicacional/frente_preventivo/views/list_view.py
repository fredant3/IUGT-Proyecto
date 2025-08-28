import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from gestion_comunicacional.frente_preventivo.services import FrentepreventivoService
from helpers.models import (
    TIPO_ACTIVIDAD,
    DESARROLLO,
)


class FrentepreventivoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "frentepreventivo.ver_frentepreventivo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion Comunicacional"
        context["submodule"] = "Frente Preventivo"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("frentepreventivo:create")
        context["listApiUrl"] = reverse_lazy("api_frentepreventivo:list")
        context["updateUrl"] = reverse_lazy("frentepreventivo:update", args=[0])
        context["deleteUrl"] = reverse_lazy("frentepreventivo:delete", args=[0])
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
                "data": "donde_desarrollo",
                "name": "donde_desarrollo",
                "title": "Donde se desarrollo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "personas_beneficiadas",
                "name": "personas_beneficiadas",
                "title": "Personas beneficiadas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "tipo_actividad",
                "name": "tipo_actividad",
                "title": "Tipo de actividad",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class FrentepreventivoListApiView(ListController, CheckPermisosMixin):
    permission_required = "frentepreventivo.ver_frentepreventivo"

    def __init__(self):
        self.service = FrentepreventivoService()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)
                tipo_actividad_mapping = dict(TIPO_ACTIVIDAD)
                desarrollo_mapping = dict(DESARROLLO)

                for item in data.get("entities", []):
                    # Mapear tipo_actividad
                    item["tipo_actividad"] = tipo_actividad_mapping.get(
                        item.get("tipo_actividad", ""), item.get("tipo_actividad", "")
                    )

                    # Mapear donde_desarrollo
                    item["donde_desarrollo"] = desarrollo_mapping.get(
                        item.get("donde_desarrollo", ""),
                        item.get("donde_desarrollo", ""),
                    )

                response.content = json.dumps(data)
            except json.JSONDecodeError:
                pass
        return response
