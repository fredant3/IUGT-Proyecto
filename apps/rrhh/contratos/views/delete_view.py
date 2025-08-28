from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import ContratoForm
from ..models import Contrato
from ..services import ContratoService
from django.contrib.messages import error
from django.core.exceptions import ObjectDoesNotExist


class ContratoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "rrhh.contratos.eliminar_contrato"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Contratos"
        context["titleForm"] = "Eliminar contrato"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("contratos:list")
        context["urlDelete"] = reverse_lazy(
            "api_contratos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Contrato.objects.filter(pk=id)


class ContratoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "rrhh.contratos.eliminar_contrato"
    form_class = ContratoForm

    def __init__(self):
        self.service = ContratoService()
