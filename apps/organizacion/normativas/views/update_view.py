from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from organizacion.normativas.forms import NormativaForm
from organizacion.normativas.models import Normativa
from organizacion.normativas.services import NormativaService


class NormativaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "organizacion.normativas.editar_normativa"
    form_class = NormativaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Normativas"
        context["titleForm"] = "Actualizar normativa"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("normativas:list")
        context["urlForm"] = reverse_lazy(
            "api_normativas:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        model = Normativa.objects.filter(pk=id)
        return model


class NormativaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "organizacion.normativas.editar_normativa"
    form_class = NormativaForm

    def __init__(self):
        self.service = NormativaService()
