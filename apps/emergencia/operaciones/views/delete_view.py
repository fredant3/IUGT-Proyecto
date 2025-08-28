from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from emergencia.operaciones.forms import EmergenciaForm
from emergencia.operaciones.models import Emergencia
from emergencia.operaciones.services import EmergenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class EmergenciaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "emergrncia.eliminar_emergencia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Operaciones"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Operaciones"
        context["titleForm"] = "Eliminar"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("operaciones:list")
        context["urlDelete"] = reverse_lazy(
            "api_operaciones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Emergencia.objects.filter(pk=id)


class EmergenciaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "emergrncia.eliminar_emergencia"
    form_class = EmergenciaForm

    def __init__(self):
        self.service = EmergenciaService()
