from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from presupuesto.partida.forms import PartidaForm
from presupuesto.partida.models import Partida
from presupuesto.partida.services import PartidaService


class PartidaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "presupuesto.partida.editar_partida"
    form_class = PartidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Partida"
        context["titleForm"] = "Actualizar partida"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("partida:list")
        context["urlForm"] = reverse_lazy(
            "api_partida:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Partida.objects.filter(pk=id)


class PartidaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.partida.editar_partida"
    form_class = PartidaForm

    def __init__(self):
        self.service = PartidaService()
