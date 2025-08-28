from administracion.inventario.forms import ArticuloForm
from administracion.inventario.models import Articulo
from administracion.inventario.services import ArticuloService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class ArticuloDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.inventario.eliminar_articulo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Inventario"
        context["titleForm"] = "Confirmar eliminación de artículo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("articulos:list")
        context["urlDelete"] = reverse_lazy(
            "api_articulos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Articulo.objects.filter(pk=id)


class ArticuloDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.inventario.eliminar_articulo"
    form_class = ArticuloForm

    def __init__(self):
        self.service = ArticuloService()
