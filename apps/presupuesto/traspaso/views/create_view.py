from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from presupuesto.cedente.services import CedenteService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from presupuesto.cedente.forms import CedenteForm

from presupuesto.receptor.forms import ReceptorForm
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect


class TraspasoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.agregar_cedente"
    form_class = CedenteForm

    def __init__(self):
        self.service = CedenteService()


class TraspasoWizardView(LoginRequiredMixin, CheckPermisosMixin, SessionWizardView):
    permission_required = "presupuesto.traspaso.agregar_cedente"
    template_name = "widzard/indextraspaso.html"
    form_list = [
        ("cedente", CedenteForm),
        ("receptor", ReceptorForm),
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["titleForm"] = "Añadir Traspaso"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("traspasos:list")

        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        # Save Cedente first
        cedente = form_dict["cedente"].save(commit=False)
        cedente.created_by = self.request.user
        cedente.save()

        # Save Receptor with the cedente relationship
        receptor = form_dict["receptor"].save(commit=False)
        receptor.cedente = cedente
        receptor.created_by = self.request.user
        receptor.save()

        return HttpResponseRedirect("/presupuesto/traspasos")
