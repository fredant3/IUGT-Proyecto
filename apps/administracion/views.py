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
        context["submodule"] = "Administración"

        context["submoduleList"] = (
            ("Asignaciones", reverse_lazy("asignaciones:list")),
            ("Averia", reverse_lazy("averias:list")),
            ("Tipo Averia", reverse_lazy("tipo_averias:list")),
            ("Compras", reverse_lazy("compras:list")),
            ("Departamentos", reverse_lazy("departamentos:list")),
            ("Inventario", reverse_lazy("articulos:list")),
            ("Sedes", reverse_lazy("sedes:list")),
        )
        return TemplateLayout.init(self, context)
