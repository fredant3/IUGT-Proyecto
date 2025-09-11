from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout
from django.contrib.auth.models import Group
from tecnologia.groups.forms import GrupoPermisosForm
from tecnologia.groups.services import GrupoPermisosService


class GroupPermisosDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Grupos"
        context["titleForm"] = "Eliminar un grupo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("grupos:list")
        context["urlDelete"] = reverse_lazy(
            "api_grupos:delete", kwargs={"pk": self.kwargs.get("pk")}
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Group.objects.filter(id=id)


class GroupPermisosDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = GrupoPermisosForm

    def __init__(self):
        self.service = GrupoPermisosService()
