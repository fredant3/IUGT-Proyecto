from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from emergencia.incidencias.forms import TipoIncidenciaForm
from emergencia.incidencias.models import TipoIncidencia
from emergencia.incidencias.services import TipoIncidenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class IncidenciasDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "emergrncia.eliminar_emergencia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipos de Incidencias"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipo de Incidencias"
        context["titleForm"] = "Eliminar"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("operaciones_incidencias:list")
        context["urlDelete"] = reverse_lazy(
            "api_operaciones_incidencias:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoIncidencia.objects.filter(pk=id)


class IncidenciasDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "emergrncia.eliminar_emergencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
