from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from planificacion.objetivos.forms import ObjetivoForm
from planificacion.objetivos.services import ObjetivoService

from templates.sneat import TemplateLayout


class ObjetivoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "planificacion.objetivos.agregar_objetivo"
    form_class = ObjetivoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Objetivos"
        context["titleForm"] = "Añadir un objetivo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("objetivos:list")
        context["urlForm"] = reverse_lazy("api_objetivos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ObjetivoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "planificacion.objetivos.agregar_objetivo"
    form_class = ObjetivoForm

    def __init__(self):
        self.service = ObjetivoService()
