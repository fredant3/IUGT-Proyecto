from potencia.tipo_incidencia.forms import TipoIncidenciaForm
from potencia.tipo_incidencia.models import TipoIncidencia
from potencia.tipo_incidencia.services import TipoIncidenciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class TipoIncidenciaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "potencia.tipoIncidencia.eliminar_tipoIncidencia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("potencia")
        context["module"] = "Potencia"
        context["submodule"] = "Tipo de Incidencia"
        context["titleForm"] = "Eliminar tipo de incidencia"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("tipoIncidencia:list")
        context["urlDelete"] = reverse_lazy(
            "api_tipoIncidencia:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoIncidencia.objects.filter(pk=id)


class TipoIncidenciaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "potencia.tipoIncidencia.eliminar_tipoIncidencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
