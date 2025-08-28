from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.receptor.forms import ReceptorForm
from presupuesto.receptor.services import ReceptorService


class ReceptorCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.receptor.agregar_receptor"
    form_class = ReceptorForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptores"
        context["titleForm"] = "Añadir un receptor"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("receptores:list")
        context["urlForm"] = reverse_lazy("api_receptores:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ReceptorCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.receptor.agregar_receptor"
    form_class = ReceptorForm

    def __init__(self):
        self.service = ReceptorService()
