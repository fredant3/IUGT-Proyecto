from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from rrhh.cargos.forms import CargoForm
from rrhh.cargos.models import Cargo
from rrhh.cargos.services import CargoService


class CargoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "rrhh.cargos.eliminar_cargo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Cargos"
        context["titleForm"] = "Eliminar cargo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("cargos:list")
        context["urlDelete"] = reverse_lazy(
            "api_cargos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Cargo.objects.filter(pk=id)


class CargoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "rrhh.cargos.eliminar_cargo"
    form_class = CargoForm

    def __init__(self):
        self.service = CargoService()
