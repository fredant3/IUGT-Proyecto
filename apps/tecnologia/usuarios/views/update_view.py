from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from templates.sneat import TemplateLayout
from tecnologia.usuarios.forms import UserForm
from users.auth.models import User
from ..services import UserService


class UserUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "user.actualizar_user"
    form_class = UserForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Usuario"
        context["titleForm"] = "Actualizar Usuarios"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("user:list")
        context["urlForm"] = reverse_lazy(
            "api_user:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return User.objects.filter(pk=id)


class UserUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "user.actualizar_user"
    form_class = UserForm

    def __init__(self):
        self.service = UserService()
