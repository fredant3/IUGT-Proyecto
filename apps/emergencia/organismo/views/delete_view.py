from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from emergencia.organismo.forms import OrganismoForm
from emergencia.organismo.models import Organismo
from emergencia.organismo.services import OrganismoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class OrganismoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "emergrncia.eliminar_emergencia"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipos de Organismo"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipo de Organismo"
        context["titleForm"] = "Eliminar"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("organismo:list")
        context["urlDelete"] = reverse_lazy(
            "api_organismo:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Organismo.objects.filter(pk=id)


class OrganismoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "emergrncia.eliminar_emergencia"
    form_class = OrganismoForm

    def __init__(self):
        self.service = OrganismoService()
