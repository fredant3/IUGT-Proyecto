from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from presupuesto.proyecto.forms import ProyectoForm
from presupuesto.proyecto.models import Proyecto
from presupuesto.proyecto.services import ProyectoService


class ProyectoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "presupuesto.proyecto.eliminar_proyecto"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Proyectos"
        context["titleForm"] = "Eliminar proyecto"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("proyectos:list")
        context["urlDelete"] = reverse_lazy(
            "api_proyectos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Proyecto.objects.filter(pk=id)


class ProyectoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "presupuesto.proyecto.eliminar_proyecto"
    form_class = ProyectoForm

    def __init__(self):
        self.service = ProyectoService()
