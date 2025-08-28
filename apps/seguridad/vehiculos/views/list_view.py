import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout

from seguridad.vehiculos.services import VehiculoService


class VehiculoListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "seguridad.vehiculos.listar_vehiculo"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Vehiculos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("vehiculos:create")
        context["listApiUrl"] = reverse_lazy("api_vehiculos:list")
        context["updateUrl"] = reverse_lazy("vehiculos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("vehiculos:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_vehiculos:export_excel")
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
                "data": "nombre",
                "name": "nombre",
                "title": "Nombre",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "apellido",
                "name": "apellido",
                "title": "Apellido",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "cedula",
                "name": "cedula",
                "title": "Cédula",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "modelo",
                "name": "modelo",
                "title": "Modelo",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "vehiculo",
                "name": "vehiculo",
                "title": "Vehículo",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "motivo",
                "name": "motivo",
                "title": "Motivo",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "capagasolina",
                "name": "capagasolina",
                "title": "Capacidad de gasolina",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "cantigasolina",
                "name": "cantigasolina",
                "title": "Cantidad de gasolina",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "placa",
                "name": "placa",
                "title": "Placa",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "fecha",
                "name": "fecha",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "true",
            },
            {
                "data": "hora",
                "name": "hora",
                "title": "Hora",
                "orderable": "false",
                "searchable": "true",
            },
        ]


class VehiculoListApiView(ListController, CheckPermisosMixin):
    permission_required = "seguridad.vehiculos.listar_vehiculo"

    def __init__(self):
        self.service = VehiculoService()
