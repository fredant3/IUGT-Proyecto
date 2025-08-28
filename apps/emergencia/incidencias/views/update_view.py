from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import TipoIncidenciaForm
from ..models import TipoIncidencia
from ..services import TipoIncidenciaService


class IncidenciasUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "emergrncia.actualizar_emergencia"
    form_class = TipoIncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipos de Incidencias"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipos de Incidencias"
        context["titleForm"] = "Actualizar"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("operaciones_incidencias:list")
        context["urlForm"] = reverse_lazy(
            "api_operaciones_incidencias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoIncidencia.objects.filter(pk=id)


class IncidenciasUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "emergrncia.actualizar_emergencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
