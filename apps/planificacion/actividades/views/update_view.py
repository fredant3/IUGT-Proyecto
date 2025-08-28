from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import ActividadForm
from ..models import Actividad
from ..services import ActividadService


class ActividadUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "planificacion.actividades.editar_actividad"
    form_class = ActividadForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Actividades"
        context["titleForm"] = "Actualizar actividad"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("actividades:list")
        context["urlForm"] = reverse_lazy(
            "api_actividades:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Actividad.objects.filter(pk=id)


class ActividadUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "planificacion.actividades.editar_actividad"
    form_class = ActividadForm

    def __init__(self):
        self.service = ActividadService()
