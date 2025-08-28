import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from tecnologia.auditoria.services import AuditoriaService


class AuditoriaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "user.ver_users"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Auditoría"
        context["listApiUrl"] = reverse_lazy("api_auditoria:list")
        context["withActions"] = False
        context["heads"] = columns
        context["columns"] = mark_safe(json.dumps(columns))
        return TemplateLayout.init(self, context)

    def getColumns(self):
        return [
            {
                "data": "id",
                "name": "id",
                "title": "#",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "ip_address",
                "name": "ip_address",
                "title": "Direccion IP",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "device_type",
                "name": "device_type",
                "title": "Dispositivo",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "browser",
                "name": "browser",
                "title": "Navegador",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "timestamp",
                "name": "timestamp",
                "title": "Fecha",
                "orderable": True,
                "searchable": True,
            },
        ]


class AuditoriaListApiView(ListController, CheckPermisosMixin):
    permission_required = "user.ver_users"

    def __init__(self):
        self.service = AuditoriaService()
