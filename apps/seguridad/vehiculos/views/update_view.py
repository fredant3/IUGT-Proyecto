from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from seguridad.vehiculos.forms import VehiculoForm
from seguridad.vehiculos.models import Vehiculo
from seguridad.vehiculos.services import VehiculoService


class VehiculoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "seguridad.vehiculos.editar_vehiculo"
    form_class = VehiculoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Vehiculos"
        context["titleForm"] = "Actualizar vehiculo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("vehiculos:list")
        context["urlForm"] = reverse_lazy(
            "api_vehiculos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Vehiculo.objects.filter(pk=id)


class VehiculoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "seguridad.vehiculos.editar_vehiculo"
    form_class = VehiculoForm

    def __init__(self):
        self.service = VehiculoService()
