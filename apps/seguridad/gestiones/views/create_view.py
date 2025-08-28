from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from seguridad.gestiones.forms import GestionForm
from seguridad.gestiones.services import GestionService


class GestionCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "seguridad.gestiones.agregar_gestion"
    form_class = GestionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Gestiones"
        context["titleForm"] = "Añadir una gestion nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gestiones:list")
        context["urlForm"] = reverse_lazy("api_gestiones:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class GestionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "seguridad.gestiones.agregar_gestion"
    form_class = GestionForm

    def __init__(self):
        self.service = GestionService()
