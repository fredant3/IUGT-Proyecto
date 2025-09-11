from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class AdministracionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Administración"
        context["submodule"] = "Inicio Administracion"
        context["data"] = [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
        context["labels"] = [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany",
        ]
        context["submoduleList"] = (
            ("Asignaciones", reverse_lazy("asignaciones:list")),
            ("Averia", reverse_lazy("averias:list")),
            ("Compras", reverse_lazy("compras:list")),
            ("Departamentos", reverse_lazy("departamentos:list")),
            ("Inventario", reverse_lazy("articulos:list")),
            ("Sedes", reverse_lazy("sedes:list")),
        )
        return TemplateLayout.init(self, context)
