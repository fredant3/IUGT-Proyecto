from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from seguridad.salidas.forms import SalidaForm
from seguridad.salidas.services import SalidaService


class SalidaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "seguridad.salidas.agregar_salida"
    form_class = SalidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Salidas"
        context["titleForm"] = "Añadir una salida nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("salidas:list")
        context["urlForm"] = reverse_lazy("api_salidas:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class SalidaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "seguridad.salidas.agregar_salida"
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
