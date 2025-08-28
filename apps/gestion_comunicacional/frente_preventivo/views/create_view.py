from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gestion_comunicacional.frente_preventivo.forms import FrentePreventivoForm
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout
from gestion_comunicacional.frente_preventivo.services import FrentepreventivoService


class FrentepreventivoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "frentepreventivo.agregar_frentepreventivo"
    form_class = FrentePreventivoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion Comunicacional"
        context["submodule"] = "Frente Preventivo"
        context["titleForm"] = "Añadir una Actividad"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("frentepreventivo:list")
        context["urlForm"] = reverse_lazy("api_frentepreventivo:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class FrentepreventivoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "frentepreventivo.agregar_frentepreventivo"
    form_class = FrentePreventivoForm

    def __init__(self):
        self.service = FrentepreventivoService()
