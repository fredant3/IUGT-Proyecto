from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import OrganismoForm
from ..models import Organismo
from ..services import OrganismoService


class OrganismoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "emergrncia.actualizar_emergencia"
    form_class = OrganismoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipos de Incidencias"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipos de Organismos"
        context["titleForm"] = "Actualizar"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("organismo:list")
        context["urlForm"] = reverse_lazy(
            "api_organismo:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Organismo.objects.filter(pk=id)


class OrganismoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "emergrncia.actualizar_emergencia"
    form_class = OrganismoForm

    def __init__(self):
        self.service = OrganismoService()
