from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import IncidenciaForm
from ..services import IncidenciaService


class IncidenciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = IncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Incidencias"
        context["titleForm"] = "Añadir una incidencia"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("incidencias:list")
        context["urlForm"] = reverse_lazy("api_incidencias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class IncidenciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = IncidenciaForm

    def __init__(self):
        self.service = IncidenciaService()
