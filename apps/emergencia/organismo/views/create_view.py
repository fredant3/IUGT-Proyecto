from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from emergencia.organismo.forms import OrganismoForm
from emergencia.organismo.services import OrganismoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from templates.sneat import TemplateLayout


class OrganismoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = OrganismoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tipo Organismo"
        context["indexUrl"] = reverse_lazy("operaciones")
        context["module"] = "Operaciones"
        context["submodule"] = "Tipos de Organismo"
        context["titleForm"] = "Añadir"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("organismo:list")
        context["urlForm"] = reverse_lazy("api_organismo:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class OrganismoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "emergrncia.agregar_emergencia"
    form_class = OrganismoForm

    def __init__(self):
        self.service = OrganismoService()
