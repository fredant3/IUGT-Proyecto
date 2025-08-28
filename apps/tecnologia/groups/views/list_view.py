import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController

from templates.sneat import TemplateLayout
from tecnologia.groups.services import GrupoPermisosService


class GroupPermisosListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Grupos"
        context["createBtn"] = "Añadir"
        context["createUrl"] = reverse_lazy("grupos:create")
        context["listApiUrl"] = reverse_lazy("api_grupos:list")
        context["updateUrl"] = reverse_lazy("grupos:update", args=[0])
        context["deleteUrl"] = reverse_lazy("grupos:delete", args=[0])
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
                "data": "name",
                "name": "name",
                "title": "Nombre",
                "orderable": "true",
                "searchable": "true",
            },
        ]


class GroupPermisosListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = GrupoPermisosService()
