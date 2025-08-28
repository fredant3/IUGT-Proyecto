from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from seguridad.entradas.forms import EntradaForm
from seguridad.entradas.models import Entrada
from seguridad.entradas.services import EntradaService


class EntradaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "seguridad.entradas.eliminar_entrada"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Entradas"
        context["titleForm"] = "Eliminar entrada"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("entradas:list")
        context["urlDelete"] = reverse_lazy(
            "api_entradas:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Entrada.objects.filter(pk=id)


class EntradaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "seguridad.entradas.eliminar_entrada"
    form_class = EntradaForm

    def __init__(self):
        self.service = EntradaService()
