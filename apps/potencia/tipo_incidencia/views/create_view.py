from potencia.tipo_incidencia.services import TipoIncidenciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from potencia.tipo_incidencia.forms import TipoIncidenciaForm
from templates.sneat import TemplateLayout


class TipoIncidenciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "potencia.tipoIncidencia.agregar_tipoIncidencia"
    form_class = TipoIncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("potencia")
        context["module"] = "Potencia"
        context["submodule"] = "Tipo de Incidencia"
        context["titleForm"] = "Añadir un tipo de incidencia"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("tipoIncidencia:list")
        context["urlForm"] = reverse_lazy("api_tipoIncidencia:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class TipoIncidenciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "potencia.tipoIncidencia.agregar_tipoIncidencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
