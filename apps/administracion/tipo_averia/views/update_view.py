from administracion.tipo_averia.forms import TipoAveriaForm
from administracion.tipo_averia.models import TipoAveria
from administracion.tipo_averia.services import TipoAveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout


class TipoAveriaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "administracion.tipo_averia.editar_tipo_averia"
    form_class = TipoAveriaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "titlePage": "Administración",
                "indexUrl": reverse_lazy("administracion"),
                "module": "Administración",
                "submodule": "Tipos de Averías",
                "titleForm": "Editar tipo de avería",
                "tag": "Guardar cambios",
                "listUrl": reverse_lazy("tipo_averias:list"),
                "urlForm": reverse_lazy(
                    "api_tipo_averias:update", args=[self.kwargs.get("pk")]
                ),
                "methodForm": "PUT",
            }
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        return TipoAveria.objects.filter(pk=self.kwargs.get("pk"))


class TipoAveriaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "administracion.tipo_averia.editar_tipo_averia"
    form_class = TipoAveriaForm

    def __init__(self):
        self.service = TipoAveriaService()
