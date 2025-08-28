from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from planificacion.actividades.forms import ActividadForm
from planificacion.actividades.models import Actividad
from planificacion.actividades.services import ActividadService

from templates.sneat import TemplateLayout


class ActividadDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "planificacion.actividades.eliminar_actividad"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Actividades"
        context["titleForm"] = "Eliminar Actividad"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("actividades:list")
        context["urlDelete"] = reverse_lazy(
            "api_actividades:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Actividad.objects.filter(pk=id)


class ActividadDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "planificacion.actividades.eliminar_actividad"
    form_class = ActividadForm

    def __init__(self):
        self.service = ActividadService()
