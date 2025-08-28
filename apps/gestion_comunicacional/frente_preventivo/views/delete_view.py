from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from gestion_comunicacional.frente_preventivo.forms import FrentePreventivoForm
from gestion_comunicacional.frente_preventivo.models import FrentePreventivo
from gestion_comunicacional.frente_preventivo.services import FrentepreventivoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class FrentepreventivoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "frentepreventivo.eliminar_frentepreventivo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente preventivo"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion Comunicacional"
        context["submodule"] = "Frente preventivo"
        context["titleForm"] = "Eliminar frente preventivo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("frentepreventivo:list")
        context["urlDelete"] = reverse_lazy(
            "api_frentepreventivo:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return FrentePreventivo.objects.filter(pk=id)


class FrentepreventivoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "frentepreventivo.eliminar_frentepreventivo"
    form_class = FrentePreventivoForm

    def __init__(self):
        self.service = FrentepreventivoService()
