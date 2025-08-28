from administracion.departamentos.forms import DepartamentoForm
from administracion.departamentos.models import Departamento
from administracion.departamentos.services import DepartamentoService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class DepartamentoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "administracion.departamentos.editar_departamento"
    form_class = DepartamentoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Departamentos"
        context["titleForm"] = "Editar departamento"
        context["tag"] = "Guardar cambios"
        context["listUrl"] = reverse_lazy("departamentos:list")
        context["urlForm"] = reverse_lazy(
            "api_departamentos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Departamento.objects.filter(pk=id)


class DepartamentoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "administracion.departamentos.editar_departamento"
    form_class = DepartamentoForm

    def __init__(self):
        self.service = DepartamentoService()
