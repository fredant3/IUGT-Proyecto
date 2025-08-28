from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from organizacion.normativas.forms import NormativaForm
from organizacion.normativas.services import NormativaService

from templates.sneat import TemplateLayout


class NormativaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "organizacion.normativas.agregar_normativa"
    form_class = NormativaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Normativas"
        context["titleForm"] = "Añadir un normativa"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("normativas:list")
        context["urlForm"] = reverse_lazy("api_normativas:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class NormativaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "organizacion.normativas.agregar_normativa"
    form_class = NormativaForm

    def __init__(self):
        self.service = NormativaService()
