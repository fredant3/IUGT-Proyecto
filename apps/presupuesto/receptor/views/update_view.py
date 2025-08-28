from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from presupuesto.receptor.forms import ReceptorForm
from presupuesto.receptor.models import Receptor
from presupuesto.receptor.services import ReceptorService


class ReceptorUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "presupuesto.receptor.editar_receptor"
    form_class = ReceptorForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Receptores"
        context["titleForm"] = "Actualizar receptor"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("receptores:list")
        context["urlForm"] = reverse_lazy(
            "api_receptores:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Receptor.objects.filter(pk=id)


class ReceptorUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.receptor.editar_receptor"
    form_class = ReceptorForm

    def __init__(self):
        self.service = ReceptorService()
