from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from emergencia.operaciones.forms import EmergenciaForm
from emergencia.operaciones.services import EmergenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout


class EmergenciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = EmergenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Operaciones"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Operaciones"
        context["titleForm"] = "Añadir"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("operaciones:list")
        context["urlForm"] = reverse_lazy("api_operaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EmergenciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = EmergenciaForm

    def __init__(self):
        self.service = EmergenciaService()
