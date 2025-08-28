from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import InfraestructuraForm
from ..models import Infraestructura
from ..services import InfraestructuraService


class InfraestructuraUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "planificacion.infraestructuras.editar_infraestructura"
    form_class = InfraestructuraForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("planificacion")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Infraestructuras"
        context["titleForm"] = "Actualizar infraestructura"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("infraestructuras:list")
        context["urlForm"] = reverse_lazy(
            "api_infraestructuras:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Infraestructura.objects.filter(pk=id)


class InfraestructuraUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "planificacion.infraestructuras.editar_infraestructura"
    form_class = InfraestructuraForm

    def __init__(self):
        self.service = InfraestructuraService()
