import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from presupuesto.acciones.models import PROYECTOS_ACCIONES
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from presupuesto.acciones.services import AccionService


class AccionListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.acciones.listar_accion"
    url_redirect = reverse_lazy("presupuesto")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Acciones"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("acciones:create")
        context["listApiUrl"] = reverse_lazy("api_acciones:list")
        context["updateUrl"] = reverse_lazy("acciones:update", args=[0])
        context["deleteUrl"] = reverse_lazy("acciones:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("acciones:export_excel")
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
                "data": "proyecto_acciones",
                "name": "proyecto_acciones",
                "title": "Proyecto o Acciones Centralizadas",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha_inicio",
                "name": "fecha_inicio",
                "title": "Inicio",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha_culminacion",
                "name": "fecha_culminacion",
                "title": "Culminación",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "situacion_presupuestaria",
                "name": "situacion_presupuestaria",
                "title": "Situación Presupuestaria",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "monto",
                "name": "monto",
                "title": "Monto Total del Proyecto",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsable_gerente",
                "name": "responsable_gerente",
                "title": "Gerente Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsable_tecnico",
                "name": "responsable_tecnico",
                "title": "Técnico Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsable_registrador",
                "name": "responsable_registrador",
                "title": "Registrador Responsable",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "responsable_administrativo",
                "name": "responsable_administrativo",
                "title": "Responsable Administrativo",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class AccionListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "presupuesto.acciones.listar_accion"
    field_mappings = {"proyecto_acciones": PROYECTOS_ACCIONES}

    def __init__(self):
        self.service = AccionService()
