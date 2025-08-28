from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from planificacion.transportes.forms import TransporteForm
from planificacion.transportes.models import Transporte
from planificacion.transportes.services import TransporteService

from templates.sneat import TemplateLayout


class TransporteDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "planificacion.transportes.eliminar_transporte"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["titleForm"] = "Eliminar transporte"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("transportes:list")
        context["urlDelete"] = reverse_lazy(
            "api_transportes:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Transporte.objects.filter(pk=id)


class TransporteDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "planificacion.transportes.eliminar_transporte"
    form_class = TransporteForm

    def __init__(self):
        self.service = TransporteService()
