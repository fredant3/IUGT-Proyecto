from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from gestion_comunicacional.forms import GestionComunicacionalForm
from gestion_comunicacional.models import GestionComunicacional
from gestion_comunicacional.services import GestioncomunicacionalService


class GestioncomunicacionalUpdateView(
    LoginRequiredMixin, CheckPermisosMixin, UpdateView
):
    permission_required = "gestioncomunicacional.actualizar_gestioncomunicacional"
    form_class = GestionComunicacionalForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion comunicacional"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion comunicacional"
        context["submodule"] = "Gestion comunicacional"
        context["titleForm"] = "Actualizar gestioncomunicacional"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gestioncomunicacional:list")
        context["urlForm"] = reverse_lazy(
            "api_gestioncomunicacional:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return GestionComunicacional.objects.filter(pk=id)


class GestioncomunicacionalUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "gestioncomunicacional.actualizar_comunicacional"
    form_class = GestionComunicacionalForm

    def __init__(self):
        self.service = GestioncomunicacionalService()
