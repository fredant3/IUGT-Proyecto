from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from planificacion.objetivos.forms import ObjetivoForm
from planificacion.objetivos.models import Objetivo
from planificacion.objetivos.services import ObjetivoService

from templates.sneat import TemplateLayout


class ObjetivoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "planificacion.objetivos.eliminar_objetivo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Objetivos"
        context["titleForm"] = "Eliminar objetivo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("objetivos:list")
        context["urlDelete"] = reverse_lazy(
            "api_objetivos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Objetivo.objects.filter(pk=id)


class ObjetivoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "planificacion.objetivos.eliminar_objetivo"
    form_class = ObjetivoForm

    def __init__(self):
        self.service = ObjetivoService()
