from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from administracion.sedes.forms import SedeForm
from administracion.sedes.services import SedeService


class SedeCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "administracion.sedes.agregar_sede"
    form_class = SedeForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Sedes"
        context["titleForm"] = "Agregar Sede"
        context["tag"] = "Registrar sede"
        context["listUrl"] = reverse_lazy("sedes:list")
        context["urlForm"] = reverse_lazy("api_sedes:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class SedeCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "administracion.sedes.agregar_sede"
    form_class = SedeForm

    def __init__(self):
        self.service = SedeService()
