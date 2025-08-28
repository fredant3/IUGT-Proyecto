from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from organizacion.reglamentos.forms import ReglamentoForm
from organizacion.reglamentos.services import ReglamentoService

from templates.sneat import TemplateLayout


class ReglamentoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "organizacion.reglamentos.agregar_reglamento"
    form_class = ReglamentoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["titleForm"] = "Añadir un reglamento"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("reglamentos:list")
        context["urlForm"] = reverse_lazy("api_reglamentos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ReglamentoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "organizacion.reglamentos.agregar_reglamento"
    form_class = ReglamentoForm

    def __init__(self):
        self.service = ReglamentoService()
