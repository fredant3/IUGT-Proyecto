import json

from administracion.compras.services import CompraService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class ComprasListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.compras.ver_compra"
    url_redirect = reverse_lazy("administracion")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Compras"
        context["createBtn"] = "Nueva compra"
        context["createUrl"] = reverse_lazy("compras:create")
        context["listApiUrl"] = reverse_lazy("api_compras:list")
        context["updateUrl"] = reverse_lazy("compras:update", args=[0])
        context["deleteUrl"] = reverse_lazy("compras:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("compras:export_excel")
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
                "data": "articulo__nombre",
                "name": "articulo__nombre",
                "title": "Articulo",
                "orderable": "true",
                "searchable": "true",
            },
            {
                "data": "n_orden",
                "name": "n_orden",
                "title": "N° de orden",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "valor_bs",
                "name": "valor_bs",
                "title": "Valor (Bs.)",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class CompraListApiView(ListController, CheckPermisosMixin):
    permission_required = "administracion.compras.ver_compra"

    def __init__(self):
        self.service = CompraService()
