from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.cedente.forms import CedenteForm
from presupuesto.cedente.services import CedenteService


class CedenteCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.cedente.agregar_cedente"
    form_class = CedenteForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Cedentes"
        context["titleForm"] = "Añadir una cedente"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("cedentes:list")
        context["urlForm"] = reverse_lazy("api_cedentes:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class CedenteCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.cedente.agregar_cedente"
    form_class = CedenteForm

    def __init__(self):
        self.service = CedenteService()
