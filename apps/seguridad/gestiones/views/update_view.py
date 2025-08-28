from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from seguridad.gestiones.forms import GestionForm
from seguridad.gestiones.models import Gestion
from seguridad.gestiones.services import GestionService


class GestionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "seguridad.gestiones.editar_gestion"
    form_class = GestionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("seguridad")
        context["module"] = "Seguridad"
        context["submodule"] = "Gestiones"
        context["titleForm"] = "Actualizar gestion"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("gestiones:list")
        context["urlForm"] = reverse_lazy(
            "api_gestiones:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Gestion.objects.filter(pk=id)


class GestionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "seguridad.gestiones.editar_gestion"
    form_class = GestionForm

    def __init__(self):
        self.service = GestionService()
