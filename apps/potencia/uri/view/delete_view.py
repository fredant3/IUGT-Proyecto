from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from potencia.uri.models import Uri
from potencia.uri.services import UriService

from templates.sneat import TemplateLayout


class UriDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "potencia.uri.eliminar_uri"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "URI"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["titleForm"] = "Eliminar incidencia"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("uri:list")
        context["urlDelete"] = reverse_lazy(
            "api_uri:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Uri.objects.filter(pk=id)


class UriDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "potencia.uri.eliminar_uri"

    def __init__(self):
        self.service = UriService()
