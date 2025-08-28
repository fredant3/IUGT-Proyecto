import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from planificacion.transportes.services import TransporteService
from helpers.BaseModelMixin import ESTADOS_CHOICES, MONTH_CHOICES


class TransporteListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion.transportes.listar_transportes"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("transportes:create")
        context["listApiUrl"] = reverse_lazy("api_transportes:list")
        context["updateUrl"] = reverse_lazy("transportes:update", args=[0])
        context["deleteUrl"] = reverse_lazy("transportes:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("transportes:export_excel")
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
                "data": "estado",
                "name": "estado",
                "title": "Estado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "mes",
                "name": "mes",
                "title": "Mes",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "transporte",
                "name": "transporte",
                "title": "Transporte",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "cantidad",
                "name": "cantidad",
                "title": "Cantidad",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class TransporteListApiView(ListController, CheckPermisosMixin):
    permission_required = "planificacion.transportes.listar_transportes"

    def __init__(self):
        self.service = TransporteService()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code == 200 and response.content:
            try:
                data = json.loads(response.content)

                # Create mappings for choices
                estado_mapping = dict(ESTADOS_CHOICES)
                mes_mapping = dict(MONTH_CHOICES)

                for item in data.get("entities", []):
                    # Convert estado code to full name
                    if "estado" in item:
                        item["estado"] = estado_mapping.get(
                            item["estado"], item["estado"]
                        )

                    # Convert month code to full name
                    if "mes" in item:
                        item["mes"] = mes_mapping.get(item["mes"], item["mes"])

                    # Ensure cantidad is a number
                    if "cantidad" in item:
                        try:
                            item["cantidad"] = int(item["cantidad"])
                        except (ValueError, TypeError):
                            item["cantidad"] = 0

                response.content = json.dumps(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
        return response
