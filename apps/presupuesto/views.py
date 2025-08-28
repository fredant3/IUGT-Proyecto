from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class PresupuestoView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Presupuesto"
        context["submodule"] = "Presupuesto"
        context["submoduleList"] = (
            ("Acciones", reverse_lazy("acciones:list")),
            ("Asignaciones", reverse_lazy("presupuesto_asignaciones:list")),
            ("Traspasos", reverse_lazy("traspasos:list")),
            ("Partida", reverse_lazy("partida:list")),
            # ("Proyectos", reverse_lazy("proyectos:list")),
            # ("Receptores", reverse_lazy("receptores:list")),
        )
        return TemplateLayout.init(self, context)
