from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from helpers.ControllerMixin import UpdateController
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout
from django.http import HttpResponseRedirect

from presupuesto.cedente.models import Cedente
from presupuesto.receptor.models import Receptor
from presupuesto.cedente.forms import CedenteForm
from presupuesto.receptor.forms import ReceptorForm


class TraspasoUpdateWizardView(
    LoginRequiredMixin, CheckPermisosMixin, SessionWizardView
):
    permission_required = "presupuesto.traspaso.editar_traspaso"
    template_name = "widzard/indextraspaso.html"
    form_list = [
        ("cedente", CedenteForm),
        ("receptor", ReceptorForm),
    ]

    def get_object_dict(self):
        cedente_id = self.kwargs.get("pk")
        cedente = Cedente.objects.get(pk=cedente_id)
        receptor = Receptor.objects.filter(cedente=cedente).first()

        return {
            "cedente": cedente,
            "receptor": receptor,
        }

    def get_form_instance(self, step):
        objects = self.get_object_dict()

        if step == "cedente":
            return objects["cedente"]
        elif step == "receptor":
            return objects["receptor"] or Receptor(cedente=objects["cedente"])
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Presupuesto"
        context["indexUrl"] = reverse_lazy("presupuesto")
        context["module"] = "Presupuesto"
        context["submodule"] = "Traspaso"
        context["titleForm"] = "Actualizar Traspaso"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("traspasos:list")
        context["action"] = "update"
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        objects = self.get_object_dict()

        # Update Cedente
        cedente_form = form_dict["cedente"]
        if cedente_form.has_changed():
            cedente_data = cedente_form.cleaned_data
            for field, value in cedente_data.items():
                setattr(objects["cedente"], field, value)
            objects["cedente"].save()

        # Update or create Receptor
        receptor_form = form_dict["receptor"]
        receptor_data = receptor_form.cleaned_data
        if objects["receptor"]:
            for field, value in receptor_data.items():
                setattr(objects["receptor"], field, value)
            objects["receptor"].save()
        else:
            Receptor.objects.create(**receptor_data, cedente=objects["cedente"])

        return HttpResponseRedirect(reverse_lazy("traspasos:list"))


class TraspasoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "presupuesto.traspaso.editar_traspaso"
    form_class = CedenteForm
