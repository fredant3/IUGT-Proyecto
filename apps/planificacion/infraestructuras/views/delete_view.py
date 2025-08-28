from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from planificacion.infraestructuras.forms import InfraestructuraForm
from planificacion.infraestructuras.models import Infraestructura
from planificacion.infraestructuras.services import InfraestructuraService

from templates.sneat import TemplateLayout


class InfraestructuraDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "planificacion.infraestructuras.eliminar_infraestructura"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Planificación"
        context["submodule"] = "Infraestructuras"
        context["titleForm"] = "Eliminar infraestructura"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("infraestructuras:list")
        context["urlDelete"] = reverse_lazy(
            "api_infraestructuras:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Infraestructura.objects.filter(pk=id)


class InfraestructuraDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "planificacion.infraestructuras.eliminar_infraestructura"
    form_class = InfraestructuraForm

    def __init__(self):
        self.service = InfraestructuraService()
