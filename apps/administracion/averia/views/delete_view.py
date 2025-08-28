from administracion.averia.forms import AveriaForm
from administracion.averia.models import Averia
from administracion.averia.services import AveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class AveriaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.averia.eliminar_averia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Averías"
        context["titleForm"] = "Confirmar eliminación"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("averias:list")
        context["urlDelete"] = reverse_lazy(
            "api_averias:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Averia.objects.filter(pk=id)


class AveriaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.averia.eliminar_averia"
    form_class = AveriaForm

    def __init__(self):
        self.service = AveriaService()
