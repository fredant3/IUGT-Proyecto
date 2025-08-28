from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from seguridad.gestiones.forms import GestionForm
from seguridad.gestiones.models import Gestion
from seguridad.gestiones.services import GestionService


class GestionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "seguridad.gestiones.eliminar_gestion"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Gestiones"
        context["titleForm"] = "Eliminar gestion"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("gestiones:list")
        context["urlDelete"] = reverse_lazy(
            "api_gestiones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Gestion.objects.filter(pk=id)


class GestionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "seguridad.gestiones.eliminar_gestion"
    form_class = GestionForm

    def __init__(self):
        self.service = GestionService()
