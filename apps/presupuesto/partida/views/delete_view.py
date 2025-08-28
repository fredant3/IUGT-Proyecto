from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from presupuesto.partida.forms import PartidaForm
from presupuesto.partida.models import Partida
from presupuesto.partida.services import PartidaService


class PartidaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "presupuesto.partida.eliminar_partida"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Partida"
        context["titleForm"] = "Eliminar partida"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("partida:list")
        context["urlDelete"] = reverse_lazy(
            "api_partida:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Partida.objects.filter(pk=id)


class PartidaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "presupuesto.partida.eliminar_partida"
    form_class = PartidaForm

    def __init__(self):
        self.service = PartidaService()
