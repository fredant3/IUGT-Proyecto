from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class GestionHumanaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "gestion_humana_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Gestión Humana"
        context["submoduleList"] = (
            ("Cargos", reverse_lazy("cargos:list")),
            ("Tipos de Sueldos", reverse_lazy("tipos_sueldos:list")),
            ("Contratos", reverse_lazy("contratos:list")),
        )
        return TemplateLayout.init(self, context)
