from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.partida.forms import PartidaForm
from presupuesto.partida.services import PartidaService


class PartidaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "presupuesto.partida.agregar_partida"
    form_class = PartidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Partida"
        context["titleForm"] = "Añadir una partida"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("partida:list")
        context["urlForm"] = reverse_lazy("api_partida:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class PartidaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.partida.agregar_partida"
    form_class = PartidaForm

    def __init__(self):
        self.service = PartidaService()
