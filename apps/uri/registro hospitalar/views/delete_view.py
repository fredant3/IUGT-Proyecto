from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from potencia.incidencias.forms import IncidenciaForm
from potencia.incidencias.models import Incidencia
from potencia.incidencias.services import IncidenciaService

from templates.sneat import TemplateLayout


class IncidenciaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Incidencias"
        context["titleForm"] = "Eliminar incidencia"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("incidencias:list")
        context["urlDelete"] = reverse_lazy(
            "api_incidencias:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Incidencia.objects.filter(pk=id)


class IncidenciaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = IncidenciaForm

    def __init__(self):
        self.service = IncidenciaService()
