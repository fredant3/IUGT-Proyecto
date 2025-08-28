from asesoria.denuncias.forms import DenunciaForm
from asesoria.denuncias.services import DenunciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class DenunciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "asesoria.denuncias.agregar_denuncia"
    form_class = DenunciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("asesoria")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["titleForm"] = "Añadir denuncia"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("denuncias:list")
        context["urlForm"] = reverse_lazy("api_denuncias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class DenunciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "asesoria.denuncias.agregar_denuncia"
    form_class = DenunciaForm

    def __init__(self):
        self.service = DenunciaService()
