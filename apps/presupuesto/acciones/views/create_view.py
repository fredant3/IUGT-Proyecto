from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.acciones.forms import AccionForm
from presupuesto.acciones.services import AccionService


class AccionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.acciones.agregar_accion"
    form_class = AccionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Acciones"
        context["titleForm"] = "Añadir una accion"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("acciones:list")
        context["urlForm"] = reverse_lazy("api_acciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class AccionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.acciones.agregar_accion"
    form_class = AccionForm

    def __init__(self):
        self.service = AccionService()
