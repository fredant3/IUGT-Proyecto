from administracion.asignaciones.forms import AsignacionForm
from administracion.asignaciones.models import Asignacion
from administracion.asignaciones.services import AsignacionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class AsignacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.asignaciones.eliminar_asignacion"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Asignaciones"
        context["titleForm"] = "Eliminar asignación"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("asignaciones:list")
        context["urlDelete"] = reverse_lazy(
            "api_asignaciones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Asignacion.objects.filter(pk=id)


class AsignacionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.asignaciones.eliminar_asignacion"
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
