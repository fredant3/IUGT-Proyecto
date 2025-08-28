from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from organizacion.normativas.forms import NormativaForm
from organizacion.normativas.models import Normativa
from organizacion.normativas.services import NormativaService

from templates.sneat import TemplateLayout


class NormativaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "organizacion.normativas.eliminar_normativa"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Normativas"
        context["titleForm"] = "Eliminar normativa"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("normativas:list")
        context["urlDelete"] = reverse_lazy(
            "api_normativas:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Normativa.objects.filter(pk=id)


class NormativaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "organizacion.normativas.eliminar_normativa"
    form_class = NormativaForm

    def __init__(self):
        self.service = NormativaService()
