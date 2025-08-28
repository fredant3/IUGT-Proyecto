from administracion.compras.forms import CompraForm
from administracion.compras.model import Compra
from administracion.compras.services import CompraService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class CompraUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "administracion.compras.editar_compra"
    form_class = CompraForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Compras"
        context["titleForm"] = "Editar compra"
        context["tag"] = "Guardar cambios"
        context["listUrl"] = reverse_lazy("compras:list")
        context["urlForm"] = reverse_lazy(
            "api_compras:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Compra.objects.filter(pk=id)


class ComprasUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "administracion.compras.editar_compra"
    form_class = CompraForm

    def __init__(self):
        self.service = CompraService()
