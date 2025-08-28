from administracion.asignaciones.forms import AsignacionForm
from administracion.asignaciones.services import AsignacionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from administracion.asignaciones.models import Asignacion

from templates.sneat import TemplateLayout


class AsignacionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = Asignacion.ADD_ARTICLE
    form_class = AsignacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Asignaciones"
        context["submodule"] = "Asignaciones"
        context["titleForm"] = "Crear nueva asignación"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("asignaciones:list")
        context["urlForm"] = reverse_lazy("api_asignaciones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class AsignacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = Asignacion.ADD_ARTICLE
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
