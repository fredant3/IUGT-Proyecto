from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class PotenciaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "potencia_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Potencia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Potencia"
        context["submodule"] = "Potencia (Energía, Infraestructura y Climatización)"
        context["submoduleList"] = (
            ("Incidencias", reverse_lazy("incidencias:list")),
            ("Tipos de Incidencias", reverse_lazy("tipoIncidencia:list")),
        )
        return TemplateLayout.init(self, context)
