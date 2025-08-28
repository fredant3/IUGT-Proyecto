from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import TransporteForm
from ..models import Transporte
from ..services import TransporteService


class TransporteUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "planificacion.transportes.editar_transporte"
    form_class = TransporteForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Transportes"
        context["titleForm"] = "Actualizar transporte"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("transportes:list")
        context["urlForm"] = reverse_lazy(
            "api_transportes:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Transporte.objects.filter(pk=id)


class TransporteUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "planificacion.transportes.editar_transporte"
    form_class = TransporteForm

    def __init__(self):
        self.service = TransporteService()
