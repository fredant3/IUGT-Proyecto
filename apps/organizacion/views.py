from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class OrganizacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "organizacion_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizaciones"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Organización"
        context["submodule"] = "Organización"
        context["submoduleList"] = (
            ("Normativas", reverse_lazy("normativas:list")),
            ("Reglamentos", reverse_lazy("reglamentos:list")),
        )
        return TemplateLayout.init(self, context)
