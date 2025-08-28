from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from seguridad.vehiculos.forms import VehiculoForm
from seguridad.vehiculos.models import Vehiculo
from seguridad.vehiculos.services import VehiculoService


class VehiculoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "seguridad.vehiculos.eliminar_vehiculo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Vehiculos"
        context["titleForm"] = "Eliminar vehiculo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("vehiculos:list")
        context["urlDelete"] = reverse_lazy(
            "api_vehiculos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Vehiculo.objects.filter(pk=id)


class VehiculoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "seguridad.vehiculos.eliminar_vehiculo"
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()
