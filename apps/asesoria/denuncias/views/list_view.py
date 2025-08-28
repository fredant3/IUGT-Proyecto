import json

from helpers.GetValueChoicesMixin import GetValueChoicesMixin
from asesoria.denuncias.services import DenunciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout
from asesoria.denuncias.models import ESTATUS_CHOICES


class DenunciaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "asesoria.denuncias.listar_denuncia"
    url_redirect = reverse_lazy("asesoría")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("asesoria")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("denuncias:create")
        context["listApiUrl"] = reverse_lazy("api_denuncias:list")
        context["updateUrl"] = reverse_lazy("denuncias:update", args=[0])
        context["deleteUrl"] = reverse_lazy("denuncias:delete", args=[0])
        context["exportExcelUrl"] = reverse_lazy("api_denuncias:export_excel")
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
                "data": "estatus",
                "name": "estatus",
                "title": "Estatus",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "ente",
                "name": "ente",
                "title": "Ente",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "denunciante_nombre",
                "name": "denunciante_nombre",
                "title": "Denunciante",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "denunciado_nombre",
                "name": "denunciado_nombre",
                "title": "Denunciado",
                "orderable": "false",
                "searchable": "false",
            },
            {
                "data": "fecha_denuncia",
                "name": "fecha_denuncia",
                "title": "Fecha",
                "orderable": "false",
                "searchable": "false",
            },
        ]


class DenunciaListApiView(GetValueChoicesMixin, ListController, CheckPermisosMixin):
    permission_required = "asesoria.denuncias.listar_denuncia"
    field_mappings = {"estatus": ESTATUS_CHOICES}

    def __init__(self):
        self.service = DenunciaService()
