from administracion.asignaciones.forms import AsignacionForm
from administracion.asignaciones.models import Asignacion
from administracion.asignaciones.services import AsignacionService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class AsignacionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "administracion.asignaciones.editar_asignacion"
    form_class = AsignacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Asignaciones"
        context["titleForm"] = "Actualizar asignación"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("asignaciones:list")
        context["urlForm"] = reverse_lazy(
            "api_asignaciones:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Asignacion.objects.filter(pk=id)


class AsignacionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "administracion.asignaciones.editar_asignacion"
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
