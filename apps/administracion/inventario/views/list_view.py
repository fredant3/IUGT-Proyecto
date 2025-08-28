import json

from administracion.inventario.services import ArticuloService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout


class ArticuloListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.inventario.listar_articulo"
    url_redirect = reverse_lazy("administracion")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Inventario"
        context["createUrl"] = reverse_lazy("articulos:create", args=[0])
        context["listApiUrl"] = reverse_lazy("api_articulos:list")
        context["updateUrl"] = reverse_lazy("articulos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("articulos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("articulos:export_excel")
        context["heads"] = columns
        context["isSelect"] = True
        context["selectTitle"] = "Registrar nuevo artículo"
        context["selectOptions"] = (
            ("tecnologia", "Tecnología"),
            ("consumible", "Consumible"),
            ("mobiliario", "Mobiliario"),
            ("vehiculo", "Vehículo"),
        )
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
                "data": "tipo_articulo__nombre",
                "name": "tipo_articulo__nombre",
                "title": "Tipo de artículo",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "marca",
                "name": "marca",
                "title": "Marca",
                "orderable": "true",
                "searchable": "false",
            },
            {
                "data": "modelo",
                "name": "modelo",
                "title": "Modelo",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha_adq",
                "name": "fecha_adq",
                "title": "Adquirido",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "codigo_bn",
                "name": "codigo_bn",
                "title": "Código de bienes",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "serial",
                "name": "serial",
                "title": "Serial",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class ArticuloListApiView(ListController, CheckPermisosMixin):
    permission_required = "administracion.inventario.listar_articulo"

    def __init__(self):
        self.service = ArticuloService()
