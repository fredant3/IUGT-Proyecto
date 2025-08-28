from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from tecnologia.groups.services import GrupoPermisosService
from templates.sneat import TemplateLayout
from tecnologia.groups.forms import GrupoPermisosForm
from django.contrib.auth.models import Group


class GroupPermisosUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = GrupoPermisosForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Grupos"
        context["titleForm"] = "Actualizar un grupo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("grupos:list")
        context["urlForm"] = reverse_lazy(
            "api_grupos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Group.objects.filter(id=id)


class GroupPermisosUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = GrupoPermisosForm

    def __init__(self):
        self.service = GrupoPermisosService()
