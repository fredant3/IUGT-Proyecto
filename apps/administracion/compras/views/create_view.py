from administracion.compras.forms import CompraForm
from administracion.compras.services import CompraService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class CompraCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "administracion.compras.agregar_compra"
    form_class = CompraForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Compras"
        context["titleForm"] = "Registrar nueva compra"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("compras:list")
        context["urlForm"] = reverse_lazy("api_compras:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class CompraCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "administracion.compras.agregar_compra"
    form_class = CompraForm

    def __init__(self):
        self.service = CompraService()
