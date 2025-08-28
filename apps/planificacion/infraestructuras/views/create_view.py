from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from planificacion.infraestructuras.forms import InfraestructuraForm
from planificacion.infraestructuras.services import InfraestructuraService

from templates.sneat import TemplateLayout


class InfraestructuraCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "planificacion.infraestructuras.agregar_infraestructura"
    form_class = InfraestructuraForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Infraestructuras"
        context["titleForm"] = "Añadir una infraestructura"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("infraestructuras:list")
        context["urlForm"] = reverse_lazy("api_infraestructuras:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class InfraestructuraCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "planificacion.infraestructuras.agregar_infraestructura"
    form_class = InfraestructuraForm

    def __init__(self):
        self.service = InfraestructuraService()
