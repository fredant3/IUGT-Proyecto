from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout
from django.views.generic import UpdateView

from organizacion.reglamentos.forms import ReglamentoForm
from organizacion.reglamentos.models import Reglamento
from organizacion.reglamentos.services import ReglamentoService


class ReglamentoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "organizacion.reglamentos.editar_reglamento"
    form_class = ReglamentoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["titleForm"] = "Actualizar reglamento"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("reglamentos:list")
        context["urlForm"] = reverse_lazy(
            "api_reglamentos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Reglamento.objects.filter(pk=id)


class ReglamentoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "organizacion.reglamentos.editar_reglamento"
    form_class = ReglamentoForm

    def __init__(self):
        self.service = ReglamentoService()
