from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from rrhh.tipos_sueldos.forms import TipoSueldoForm
from rrhh.tipos_sueldos.models import TipoSueldo
from rrhh.tipos_sueldos.services import TipoSueldoService


class TipoSueldoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "rrhh.tipos_sueldos.editar_tipo_sueldo"
    form_class = TipoSueldoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Tipos de sueldos"
        context["titleForm"] = "Actualizar tipo de sueldo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("tipos_sueldos:list")
        context["urlForm"] = reverse_lazy(
            "api_tipos_sueldos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return TipoSueldo.objects.filter(pk=id)


class TipoSueldoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "rrhh.tipos_sueldos.editar_tipo_sueldo"
    form_class = TipoSueldoForm

    def __init__(self):
        self.service = TipoSueldoService()
