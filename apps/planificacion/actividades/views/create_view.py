from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from planificacion.actividades.forms import ActividadForm
from planificacion.actividades.services import ActividadService

from templates.sneat import TemplateLayout


class ActividadCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "planificacion.actividades.agregar_actividad"
    form_class = ActividadForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Actividad"
        context["titleForm"] = "Añadir una actividad"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("actividades:list")
        context["urlForm"] = reverse_lazy("api_actividades:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ActividadCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "planificacion.actividades.agregar_actividad"
    form_class = ActividadForm

    def __init__(self):
        self.service = ActividadService()
