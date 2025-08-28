from potencia.tipo_incidencia.forms import TipoIncidenciaForm
from potencia.tipo_incidencia.models import TipoIncidencia
from potencia.tipo_incidencia.services import TipoIncidenciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class TipoIncidenciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "potencia.tipoIncidencia.editar_tipoIncidencia"
    form_class = TipoIncidenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("potencia")
        context["module"] = "Potencia"
        context["submodule"] = "Tipo de Incidencia"
        context["titleForm"] = "Actualizar"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("tipoIncidencia:list")
        context["urlForm"] = reverse_lazy(
            "api_tipoIncidencia:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoIncidencia.objects.filter(pk=id)


class TipoIncidenciaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "potencia.tipoIncidencia.editar_tipoIncidencia"
    form_class = TipoIncidenciaForm

    def __init__(self):
        self.service = TipoIncidenciaService()
