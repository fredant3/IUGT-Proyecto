from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from gestion_comunicacional.forms import GestionComunicacionalForm
from gestion_comunicacional.models import GestionComunicacional
from gestion_comunicacional.services import GestioncomunicacionalService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class GestioncomunicacionalDeleteView(
    LoginRequiredMixin, CheckPermisosMixin, DeleteView
):
    permission_required = "gestioncomunicacional.eliminar_gestioncomunicacional"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion comunicacional"
        context["indexUrl"] = reverse_lazy("gc_info")
        context["module"] = "Gestion comunicacional"
        context["submodule"] = "Gestion comunicacional"
        context["titleForm"] = "Eliminar gestion comunicacional"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gestioncomunicacional:list")
        context["urlDelete"] = reverse_lazy(
            "api_gestioncomunicacional:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return GestionComunicacional.objects.filter(pk=id)


class GestioncomunicacionalDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "gestioncomunicacional.eliminar_gestioncomunicacional"
    form_class = GestionComunicacionalForm

    def __init__(self):
        self.service = GestioncomunicacionalService()
