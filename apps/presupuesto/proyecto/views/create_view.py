from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.proyecto.forms import ProyectoForm
from presupuesto.proyecto.services import ProyectoService


class ProyectoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.proyecto.agregar_proyecto"
    form_class = ProyectoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Proyectos"
        context["titleForm"] = "Añadir un proyecto"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("proyectos:list")
        context["urlForm"] = reverse_lazy("api_proyectos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ProyectoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.proyecto.agregar_proyecto"
    form_class = ProyectoForm

    def __init__(self):
        self.service = ProyectoService()
