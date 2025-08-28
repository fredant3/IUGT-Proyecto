from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController
from organizacion.reglamentos.forms import ReglamentoForm
from organizacion.reglamentos.models import Reglamento
from organizacion.reglamentos.services import ReglamentoService

from templates.sneat import TemplateLayout


class ReglamentoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "organizacion.reglamentos.eliminar_reglamento"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["titleForm"] = "Eliminar reglamento"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("reglamentos:list")
        context["urlDelete"] = reverse_lazy(
            "api_reglamentos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Reglamento.objects.filter(pk=id)


class ReglamentoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "organizacion.reglamentos.eliminar_reglamento"
    form_class = ReglamentoForm

    def __init__(self):
        self.service = ReglamentoService()
