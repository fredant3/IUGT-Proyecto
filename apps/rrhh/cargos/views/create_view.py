from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from rrhh.cargos.forms import CargoForm
from rrhh.cargos.services import CargoService


class CargoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "rrhh.cargos.agregar_cargo"
    form_class = CargoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Cargos"
        context["titleForm"] = "Añadir una cargo nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("cargos:list")
        context["urlForm"] = reverse_lazy("api_cargos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class CargoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "rrhh.cargos.agregar_cargo"
    form_class = CargoForm

    def __init__(self):
        self.service = CargoService()
