from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class AsesoriaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "asesoria_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría"
        context["submodule"] = "Asesoría Jurídica"
        context["submoduleList"] = (
            ("Denuncias", reverse_lazy("denuncias:list")),
            ("Fílmicos", reverse_lazy("filmicos:list")),
        )
        return TemplateLayout.init(self, context)
