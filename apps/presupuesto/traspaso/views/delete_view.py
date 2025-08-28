from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from presupuesto.cedente.forms import CedenteForm
from presupuesto.cedente.services import CedenteService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from presupuesto.cedente.models import Cedente


class TraspasoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "presupuesto.traspaso.eliminar_traspaso"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["titleForm"] = "Eliminar traspaso"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("traspasos:list")
        context["urlDelete"] = reverse_lazy(
            "api_traspasos:delete", kwargs={"pk": self.kwargs.get("pk")}
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cedente.objects.filter(pk=id)


class TraspasoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.eliminar_traspaso"
    form_class = CedenteForm

    def __init__(self):
        self.service = CedenteService()
