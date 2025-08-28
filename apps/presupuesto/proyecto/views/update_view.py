from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from presupuesto.proyecto.forms import ProyectoForm
from presupuesto.proyecto.models import Proyecto
from presupuesto.proyecto.services import ProyectoService


class ProyectoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "presupuesto.proyecto.editar_proyecto"
    form_class = ProyectoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Proyectos"
        context["titleForm"] = "Actualizar proyecto"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("proyectos:list")
        context["urlForm"] = reverse_lazy(
            "api_proyectos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Proyecto.objects.filter(pk=id)


class ProyectoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.proyecto.editar_proyecto"
    form_class = ProyectoForm

    def __init__(self):
        self.service = ProyectoService()
