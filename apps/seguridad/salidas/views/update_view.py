from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from seguridad.salidas.forms import SalidaForm
from seguridad.salidas.models import Salida
from seguridad.salidas.services import SalidaService


class SalidaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "seguridad.salidas.editar_salida"
    form_class = SalidaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Salidas"
        context["titleForm"] = "Actualizar salida"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("salidas:list")
        context["urlForm"] = reverse_lazy(
            "api_salidas:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Salida.objects.filter(pk=id)


class SalidaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "seguridad.salidas.editar_salida"
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
