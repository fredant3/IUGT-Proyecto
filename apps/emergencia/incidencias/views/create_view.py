from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from emergencia.incidencias.forms import TipoIncidenciaForm
from emergencia.incidencias.services import TipoIncidenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout


class IncidenciasCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = TipoIncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipo Incidencias"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipos de Incidencias"
        context["titleForm"] = "Registrar"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("operaciones_incidencias:list")
        context["urlForm"] = reverse_lazy("api_operaciones_incidencias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class IncidenciasCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
