from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from seguridad.entradas.forms import EntradaForm
from seguridad.entradas.services import EntradaService


class EntradaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "seguridad.entradas.agregar_entrada"
    form_class = EntradaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Entradas"
        context["titleForm"] = "Añadir una entrada nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("entradas:list")
        context["urlForm"] = reverse_lazy("api_entradas:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EntradaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "seguridad.entradas.agregar_entrada"
    form_class = EntradaForm

    def __init__(self):
        self.service = EntradaService()
