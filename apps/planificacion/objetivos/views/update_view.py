from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import ObjetivoForm
from ..models import Objetivo
from ..services import ObjetivoService


class ObjetivoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "planificacion.objetivos.editar_objetivo"
    form_class = ObjetivoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Objetivos"
        context["titleForm"] = "Actualizar objetivo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("objetivos:list")
        context["urlForm"] = reverse_lazy(
            "api_objetivos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Objetivo.objects.filter(pk=id)


class ObjetivoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "planificacion.objetivos.editar_objetivo"
    form_class = ObjetivoForm

    def __init__(self):
        self.service = ObjetivoService()
