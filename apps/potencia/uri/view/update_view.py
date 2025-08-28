from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout
from django.http import HttpResponseRedirect

from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from potencia.uri.models import Uri
from potencia.uri.forms import (
    UriInfoGeneralForm,
    UriInfolegalForm,
    UripacienteForm,
    UriConsentimientoForm,
    UriDireccionForm,
    UriInfoclinicaForm,
    UriSignosVitalesForm,
    UriReferenciasForm,
)


class UriUpdateWizardView(LoginRequiredMixin, CheckPermisosMixin, SessionWizardView):
    permission_required = "potencia.uri.editar_uri"
    template_name = "widzard/index.html"
    form_list = [
        ("general", UriInfoGeneralForm),
        ("legal", UriInfolegalForm),
        ("paciente", UripacienteForm),
        ("consentimiento", UriConsentimientoForm),
        ("direccion", UriDireccionForm),
        ("clinica", UriInfoclinicaForm),
        ("signos", UriSignosVitalesForm),
        ("referencias", UriReferenciasForm),
    ]

    def get_object(self):
        uri_id = self.kwargs.get("pk")
        return Uri.objects.get(pk=uri_id)

    def get_form_instance(self, step):
        uri = self.get_object()
        return uri  # Todas las forms comparten la misma instancia Uri

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Actualizar URI"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["action"] = "update"
        context["uri_id"] = self.kwargs.get("pk")
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        uri = self.get_object()

        # Actualizar todos los campos de todas las forms
        for form in form_dict.values():
            for field, value in form.cleaned_data.items():
                setattr(uri, field, value)

        uri.save()
        return HttpResponseRedirect("/uri/unidad-respuesta-inmediata")


class UriUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "potencia.uri.editar_uri"
    form_class = UriInfoGeneralForm

    def __init__(self):
        from potencia.uri.services import UriService

        self.service = UriService()
