from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from presupuesto.receptor.forms import ReceptorForm
from presupuesto.receptor.models import Receptor
from presupuesto.receptor.services import ReceptorService


class ReceptorDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "presupuesto.receptor.eliminar_receptor"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptores"
        context["titleForm"] = "Eliminar receptor"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("receptores:list")
        context["urlDelete"] = reverse_lazy(
            "api_receptores:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Receptor.objects.filter(pk=id)


class ReceptorDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "presupuesto.receptor.eliminar_receptor"
    form_class = ReceptorForm

    def __init__(self):
        self.service = ReceptorService()
