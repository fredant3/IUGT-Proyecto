import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import ListController
from organizacion.normativas.services import NormativaService

from templates.sneat import TemplateLayout


class NormativaListView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("bibliotecas")
    template_name = "biblioteca/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["indexUrl"] = reverse_lazy("bibliotecas")
        context["titlePage"] = "Biblioteca"
        context["module"] = "Biblioteca"
        context["submodule"] = "Normativas"
        context["submodules"] = json.dumps(
            (
                {
                    "api": "{0}?order[0][name]=date&order[0][dir]=desc&columns[0][searchable]=true&columns[0][name]=estado&columns[0]".format(
                        str(reverse_lazy("api_biblioteca_normativas:list"))
                    ),
                    "name": "Normativas",
                },
            )
        )
        return TemplateLayout.init(self, context)


class NormativaListApiView(ListController, CheckPermisosMixin):
    permission_required = ""

    def __init__(self):
        self.service = NormativaService()
