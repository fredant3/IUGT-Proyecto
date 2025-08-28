from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from seguridad.salidas.forms import SalidaForm
from seguridad.salidas.models import Salida
from seguridad.salidas.services import SalidaService


class SalidaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "seguridad.salidas.eliminar_salida"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Salidas"
        context["titleForm"] = "Eliminar salida"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("salidas:list")
        context["urlDelete"] = reverse_lazy(
            "api_salidas:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Salida.objects.filter(pk=id)


class SalidaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "seguridad.salidas.eliminar_salida"
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
