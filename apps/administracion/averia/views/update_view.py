from administracion.averia.forms import AveriaForm
from administracion.averia.models import Averia
from administracion.averia.services import AveriaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class AveriaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "administracion.averia.editar_averia"
    form_class = AveriaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administración"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administración"
        context["submodule"] = "Averías"
        context["titleForm"] = "Editar avería"
        context["tag"] = "Guardar cambios"
        context["listUrl"] = reverse_lazy("averias:list")
        context["urlForm"] = reverse_lazy(
            "api_averias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Averia.objects.filter(pk=id)


class AveriaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "administracion.averia.editar_averia"
    form_class = AveriaForm

    def __init__(self):
        self.service = AveriaService()
