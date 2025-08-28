from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from planificacion.transportes.forms import TransporteForm
from planificacion.transportes.services import TransporteService

from templates.sneat import TemplateLayout


class TransporteCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "planificacion.transportes.agregar_transporte"
    form_class = TransporteForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["titleForm"] = "Añadir una transporte"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("transportes:list")
        context["urlForm"] = reverse_lazy("api_transportes:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TransporteCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "planificacion.transportes.agregar_transporte"
    form_class = TransporteForm

    def __init__(self):
        self.service = TransporteService()
