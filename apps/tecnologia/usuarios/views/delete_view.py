from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from tecnologia.usuarios.forms import UserForm
from users.auth.models import User
from tecnologia.usuarios.services import UserService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class UserDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "user.eliminar_user"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Usuario"
        context["titleForm"] = "Eliminar user"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("user:list")
        context["urlDelete"] = reverse_lazy(
            "api_user:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return User.objects.filter(pk=id)


class UserDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "user.eliminar_user"
    form_class = UserForm

    def __init__(self):
        self.service = UserService()
