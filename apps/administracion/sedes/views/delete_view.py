from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from administracion.sedes.forms import SedeForm
from administracion.sedes.models import Sede
from administracion.sedes.services import SedeService


class SedeDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "administracion.sedes.eliminar_sede"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Sedes"
        context["titleForm"] = "Eliminar sede"
        context["tag"] = "Eliminar sede"
        context["listUrl"] = reverse_lazy("sedes:list")
        context["urlDelete"] = reverse_lazy(
            "api_sedes:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Sede.objects.filter(pk=id)


class SedeDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "administracion.sedes.eliminar_sede"
    form_class = SedeForm

    def __init__(self):
        self.service = SedeService()
