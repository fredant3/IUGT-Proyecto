import json
from administracion.averia.services import AveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.BaseModelMixin import DEP_AVERIA
from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout


class AveriaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.averia.listar_averia"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Averías"
        context["createBtn"] = "Nueva avería"
        context["createUrl"] = reverse_lazy("averias:create")
        context["listApiUrl"] = reverse_lazy("api_averias:list")
        context["updateUrl"] = reverse_lazy("averias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("averias:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("averias:export_excel")
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
                "searchable": "false",
            },
            {
                "data": "problema",
                "name": "problema",
                "title": "Problema",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "tipo_averia__nombre",
                "name": "tipo_averia__nombre",
                "title": "Tipo de avería",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "departamento__nombre",
                "name": "departamento__nombre",
                "title": "Departamento",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Número de serie",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "codigo_bn",
                "name": "codigo_bn",
                "title": "Código BN",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "d_averia",
                "name": "d_averia",
                "title": "Departamento Averia",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class AveriaListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "administracion.averia.listar_averia"
    field_mappings = {"d_averia": DEP_AVERIA}

    def __init__(self):
        self.service = AveriaService()
