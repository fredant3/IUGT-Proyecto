import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout


class BibliotecatView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "biblioteca_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "biblioteca/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Biblioteca"
        context["module"] = "Biblioteca"
        context["buttons"] = [
            {
                "name": "Normativas",
                "url": reverse_lazy("biblioteca_normativas:list"),
                "class": "btn-primary",
            },
            {
                "name": "Reglamentos",
                "url": reverse_lazy("biblioteca_reglamentos:list"),
                "class": "btn-success",
            },
        ]
        return TemplateLayout.init(self, context)
