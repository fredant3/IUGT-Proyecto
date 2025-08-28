from asesoria.filmicos.models import RegistroFilmico
from asesoria.filmicos.services import RegistroFilmicoService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class RegistroFilmicoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "asesoria.filmicos.eliminar_registroFilmico"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("asesoria")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Registro Fílmico"
        context["titleForm"] = "Eliminar registro fílmico"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("filmicos:list")
        context["urlDelete"] = reverse_lazy(
            "api_filmicos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return RegistroFilmico.objects.filter(pk=id)


class RegistroFilmicoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "asesoria.filmicos.eliminar_registroFilmico"

    def __init__(self):
        self.service = RegistroFilmicoService()
