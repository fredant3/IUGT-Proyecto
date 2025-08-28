from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class PlanificacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "planificacion_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Planificación"
        context["submoduleList"] = (
            ("Objetivos", reverse_lazy("objetivos:list")),
            ("Actividades", reverse_lazy("actividades:list")),
            # ("Infraestructuras", reverse_lazy("infraestructuras:list")),
            # ("Transportes", reverse_lazy("transportes:list")),
        )
        return TemplateLayout.init(self, context)
