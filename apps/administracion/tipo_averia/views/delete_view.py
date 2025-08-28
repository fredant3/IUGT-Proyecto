from administracion.tipo_averia.forms import TipoAveriaForm
from administracion.tipo_averia.models import TipoAveria
from administracion.tipo_averia.services import TipoAveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from templates.sneat import TemplateLayout


class TipoAveriaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.tipo_averia.eliminar_tipo_averia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "titlePage": "Administración",
                "indexUrl": reverse_lazy("administracion"),
                "module": "Administración",
                "submodule": "Tipos de Averías",
                "titleForm": "Confirmar eliminación",
                "tag": "Eliminar",
                "listUrl": reverse_lazy("tipo_averias:list"),
                "urlDelete": reverse_lazy(
                    "api_tipo_averias:delete", args=[self.kwargs.get("pk")]
                ),
            }
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        return TipoAveria.objects.filter(pk=self.kwargs.get("pk"))


class TipoAveriaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.tipo_averia.eliminar_tipo_averia"
    form_class = TipoAveriaForm

    def __init__(self):
        self.service = TipoAveriaService()
