from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout
from tecnologia.groups.forms import GrupoPermisosForm
from tecnologia.groups.services import GrupoPermisosService


class GroupPermisosCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = GrupoPermisosForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Grupos"
        context["titleForm"] = "Añadir un grupo nuevo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("grupos:list")
        context["urlForm"] = reverse_lazy("api_grupos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class GroupPermisosCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = GrupoPermisosForm

    def __init__(self):
        self.service = GrupoPermisosService()
