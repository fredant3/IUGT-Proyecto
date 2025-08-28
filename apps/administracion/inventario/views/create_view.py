from administracion.inventario.forms import ArticuloForm
from administracion.inventario.helper import define_type_form
from administracion.inventario.services import ArticuloService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class ArticuloCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "administracion.inventario.agregar_articulo"
    template_name = "sneat/layout/partials/form/layout.html"
    form_class = ArticuloForm

    def get_form_class(self):
        return define_type_form(self.kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Inventario"
        context["titleForm"] = (
            f"Registrar nuevo artículo - {str(self.kwargs.get('type')).capitalize()}"
        )
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("articulos:list")
        context["urlForm"] = reverse_lazy(
            "api_articulos:create", args=[self.kwargs.get("type")]
        )
        context["methodForm"] = "POST"
        self.form_class = define_type_form(self.kwargs)
        return TemplateLayout.init(self, context)


class ArtiluloCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "administracion.inventario.agregar_articulo"
    form_class = ArticuloForm

    def __init__(self):
        self.service = ArticuloService()

    def get_initial(self):
        initial = super().get_initial()
        initial["tipo_articulo_id"] = define_type_form(self.kwargs)
        return initial
