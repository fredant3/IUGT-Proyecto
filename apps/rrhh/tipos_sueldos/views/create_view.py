from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.forms import TipoSueldoForm
from rrhh.tipos_sueldos.services import TipoSueldoService


class TipoSueldoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.tipos_sueldos.agregar_tipo_sueldo"
    form_class = TipoSueldoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Tipos de Sueldos"
        context["titleForm"] = "Añadir un tipo de empleado nuevo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("tipos_sueldos:list")
        context["urlForm"] = reverse_lazy("api_tipos_sueldos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TipoSueldoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_sueldos.eliminar_tipo_sueldo"
    form_class = TipoSueldoForm

    def __init__(self):
        self.service = TipoSueldoService()
