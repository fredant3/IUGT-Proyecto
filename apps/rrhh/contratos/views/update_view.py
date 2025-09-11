from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout
from django.http import HttpResponseRedirect

from rrhh.empleados.models import Empleado
from rrhh.contratos.models import Contrato
from rrhh.educaciones.models import Educacion
from rrhh.familiares.models import Familiar
from rrhh.dotaciones.models import Dotacion

from rrhh.contratos.forms import ContratoForm
from rrhh.empleados.forms import EmpleadoForm
from rrhh.educaciones.forms import EducacionForm
from rrhh.familiares.forms import FamiliarForm
from rrhh.dotaciones.forms import DotacionForm

from helpers.ControllerMixin import UpdateController
from rrhh.contratos.services import ContratoService


class ContratoUpdateWizardView(
    LoginRequiredMixin, CheckPermisosMixin, SessionWizardView
):
    permission_required = "rrhh.contratos.editar_contrato"
    template_name = "widzard/indexrrhh.html"
    form_list = [
        ("empleado", EmpleadoForm),
        ("educacion", EducacionForm),
        ("familiar", FamiliarForm),
        ("dotacion", DotacionForm),
        ("contrato", ContratoForm),
    ]

    def get_object_dict(self):
        contract_id = self.kwargs.get("pk")
        contract = Contrato.objects.get(pk=contract_id)
        employee = contract.empleado

        education = Educacion.objects.filter(empleado=employee).first()
        family = Familiar.objects.filter(empleado=employee).first()
        dotacion = Dotacion.objects.filter(empleado=employee).first()

        return {
            "contract": contract,
            "employee": employee,
            "education": education,
            "family": family,
            "dotacion": dotacion,
        }

    def get_form_instance(self, step):
        objects = self.get_object_dict()

        if step == "empleado":
            return objects["employee"]
        elif step == "educacion":
            return objects["education"] or Educacion(empleado=objects["employee"])
        elif step == "familiar":
            return objects["family"] or Familiar(empleado=objects["employee"])
        elif step == "dotacion":
            return objects["dotacion"] or Dotacion(empleado=objects["employee"])
        elif step == "contrato":
            return objects["contract"]
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Actualizar Contrato"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Contrato"
        context["action"] = "update"
        context["contract_id"] = self.kwargs.get("pk")
        return TemplateLayout.init(self, context)

    def done(self, form_list, form_dict, **kwargs):
        objects = self.get_object_dict()

        # Procesar empleado
        employee_form = form_dict["empleado"]
        employee_data = employee_form.cleaned_data
        if employee_form.has_changed():
            for field, value in employee_data.items():
                setattr(objects["employee"], field, value)
            objects["employee"].save()

            if hasattr(objects["employee"], "usuario") and objects["employee"].usuario:
                user = objects["employee"].usuario
                if "cedula" in employee_data:
                    user.username = employee_data["cedula"]
                    user.dni = employee_data["cedula"]
                user.save()

        # Procesar educación
        education_form = form_dict["educacion"]
        education_data = education_form.cleaned_data
        if objects["education"]:
            for field, value in education_data.items():
                setattr(objects["education"], field, value)
            objects["education"].save()
        else:
            Educacion.objects.create(**education_data, empleado=objects["employee"])

        # Procesar familiar
        family_form = form_dict["familiar"]
        family_data = family_form.cleaned_data
        if objects["family"]:
            for field, value in family_data.items():
                setattr(objects["family"], field, value)
            objects["family"].save()
        else:
            Familiar.objects.create(**family_data, empleado=objects["employee"])

        # Procesar dotación
        dotacion_form = form_dict["dotacion"]
        dotacion_data = dotacion_form.cleaned_data
        if objects["dotacion"]:
            for field, value in dotacion_data.items():
                setattr(objects["dotacion"], field, value)
            objects["dotacion"].save()
        else:
            Dotacion.objects.create(**dotacion_data, empleado=objects["employee"])

        # Procesar contrato
        contract_form = form_dict["contrato"]
        if contract_form.has_changed():
            contract_data = contract_form.cleaned_data
            for field, value in contract_data.items():
                setattr(objects["contract"], field, value)
            objects["contract"].save()

        return HttpResponseRedirect(reverse_lazy("contratos:list"))


class ContratoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "rrhh.contratos.editar_contrato"
    form_class = ContratoForm

    def __init__(self):
        self.service = ContratoService()
