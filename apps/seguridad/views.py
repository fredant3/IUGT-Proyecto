from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class SeguridadView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Seguridad"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Seguridad"
        context["submodule"] = "Seguridad"
        context["submoduleList"] = (
            ("Entradas", reverse_lazy("entradas:list")),
            ("Gestiones", reverse_lazy("gestiones:list")),
            ("Salidas", reverse_lazy("salidas:list")),
            ("Vehiculos", reverse_lazy("vehiculos:list")),
        )
        return TemplateLayout.init(self, context)
