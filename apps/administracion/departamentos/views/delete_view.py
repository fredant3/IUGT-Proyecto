from administracion.departamentos.forms import DepartamentoForm
from administracion.departamentos.models import Departamento
from administracion.departamentos.services import DepartamentoService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class DepartamentoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.departamentos.eliminar_departamento"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Departamentos"
        context["titleForm"] = "Confirmar eliminación"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("departamentos:list")
        context["urlDelete"] = reverse_lazy(
            "api_departamentos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Departamento.objects.filter(pk=id)


class DepartamentoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.departamentos.eliminar_departamento"
    form_class = DepartamentoForm

    def __init__(self):
        self.service = DepartamentoService()
