from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gestion_comunicacional.forms import GestionComunicacionalForm
from gestion_comunicacional.services import GestioncomunicacionalService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout


class GestioncomunicacionalCreateView(
    LoginRequiredMixin, CheckPermisosMixin, CreateView
):
    permission_required = "gestioncomunicacional.agregar_gestion_comunicacional"
    form_class = GestionComunicacionalForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Comunicacional"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion Comunicacional"
        context["submodule"] = "Gestion Comunicacional"
        context["titleForm"] = "Añadir una Actividad"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gestioncomunicacional:list")
        context["urlForm"] = reverse_lazy("api_gestioncomunicacional:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class GestioncomunicacoinalCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "gestionalcomunicacional.agregar_gestioncomunicacional"
    form_class = GestionComunicacionalForm

    def __init__(self):
        self.service = GestioncomunicacionalService()
