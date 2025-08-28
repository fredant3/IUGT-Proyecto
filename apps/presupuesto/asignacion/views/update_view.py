from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from presupuesto.asignacion.forms import AsignacionForm
from presupuesto.asignacion.models import Asignacion
from presupuesto.asignacion.services import AsignacionService


class AsignacionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "presupuesto.asignacion.editar_asignacion"
    form_class = AsignacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Asignaciones"
        context["titleForm"] = "Actualizar accion"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("presupuesto_asignaciones:list")
        context["urlForm"] = reverse_lazy(
            "api_presupuesto_asignaciones:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Asignacion.objects.filter(pk=id)


class AsignacionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.asignacion.editar_asignacion"
    form_class = AsignacionForm

    def __init__(self):
        self.service = AsignacionService()
