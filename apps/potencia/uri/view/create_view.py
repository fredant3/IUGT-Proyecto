from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from formtools.wizard.views import SessionWizardView
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
from templates.sneat import TemplateLayout
from django.http import HttpResponseRedirect
from potencia.uri.models import Uri


class UriCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "potencia.uri.agregar_uri"
    form_class = UriInfoGeneralForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "URI"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        context["titleForm"] = "Añadir registro"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("uri:list")
        context["urlForm"] = reverse_lazy("api_uri:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class UriCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "potencia.uri.agregar_uri"
    form_class = UriInfoGeneralForm


class InfogeneralWizardView(SessionWizardView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "URI"
        context["indexUrl"] = reverse_lazy("uri:list")
        context["module"] = "URI"
        context["submodule"] = "Unidad de Respuesta Inmediata"
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        datos_generales = form_dict["general"].cleaned_data
        datos_legal = form_dict["legal"].cleaned_data
        datos_paciente = form_dict["paciente"].cleaned_data
        datos_consentimiento = form_dict["consentimiento"].cleaned_data
        datos_direccion = form_dict["direccion"].cleaned_data
        datos_clinica = form_dict["clinica"].cleaned_data
        datos_signos = form_dict["signos"].cleaned_data
        datos_referencias = form_dict["referencias"].cleaned_data

        registro = Uri(
            **datos_generales,
            **datos_legal,
            **datos_paciente,
            **datos_consentimiento,
            **datos_direccion,
            **datos_clinica,
            **datos_signos,
            **datos_referencias
        )

        print("========================================")
        print(registro)
        print("========================================")

        registro.save()
        return HttpResponseRedirect("/uri/unidad-respuesta-inmediata")

    # def __init__(self):
    # self.service = UriService()
