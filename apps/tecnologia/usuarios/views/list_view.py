import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from django.http import JsonResponse
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from templates.sneat import TemplateLayout
from tecnologia.usuarios.services import UserService


class UserListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "user.ver_users"
    url_redirect = reverse_lazy("modules:index")
    template_name = "sneat/layout/partials/data-table/layout.html"

    def get_context_data(self, **kwargs):
        columns = self.getColumns()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Usuario"
        context["listApiUrl"] = reverse_lazy("api_user:list")
        context["updateUrl"] = reverse_lazy("user:update", args=[0])
        context["deleteUrl"] = reverse_lazy("user:delete", args=[0])
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
                "data": "username",
                "name": "username",
                "title": "Usuario",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "empleado_nombre",
                "name": "empleado_nombre",
                "title": "Empleado",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "empleado_cedula",
                "name": "empleado_cedula",
                "title": "Cédula",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "tipo_contrato",
                "name": "tipo_contrato",
                "title": "Tipo Contrato",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "estatus_contrato",
                "name": "estatus_contrato",
                "title": "Estatus Contrato",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "departamento",
                "name": "departamento",
                "title": "Departamento",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "cargo",
                "name": "cargo",
                "title": "Cargo",
                "orderable": True,
                "searchable": True,
            },
            {
                "data": "is_active",
                "name": "is_active",
                "title": "Estatus Usuario",
                "orderable": True,
                "searchable": True,
            },
        ]


class UserListApiView(ListController, CheckPermisosMixin):
    permission_required = "user.ver_users"

    def __init__(self):
        self.service = UserService()

    def get(self, request, *args, **kwargs):
        data = {}
        draw = int(self.request.GET.get("draw")) if self.request.GET.get("draw") else 1
        start = (
            int(self.request.GET.get("start")) if self.request.GET.get("start") else 0
        )
        length = (
            int(self.request.GET.get("length"))
            if self.request.GET.get("length")
            else 10
        )
        search = self.request.GET.get("search[value]") or None
        try:
            data = self.service.get_all_with_related_info(draw, start, length, search)
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)
