from asesoria.denuncias.forms import DenunciaForm
from asesoria.denuncias.models import Denuncia
from asesoria.denuncias.services import DenunciaService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class DenunciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "asesoria.denuncias.editar_denuncia"
    form_class = DenunciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("asesoria")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["titleForm"] = "Actualizar denuncia"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("denuncias:list")
        context["urlForm"] = reverse_lazy(
            "api_denuncias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Denuncia.objects.filter(pk=id)

    def get_initial(self):
        return self.cargar_datos_iniciales(self.object)

    def cargar_datos_iniciales(self, denuncia):
        if denuncia:
            return {
                "nombres_denunciante": denuncia.denunciante.nombres,
                "apellidos_denunciante": denuncia.denunciante.apellidos,
                "cedula_denunciante": denuncia.denunciante.cedula,
                "telefono_denunciante": denuncia.denunciante.telefono,
                "email_denunciante": denuncia.denunciante.email,
                "direccion_denunciante": denuncia.denunciante.direccion,
                "nombres_denunciado": denuncia.denunciado.nombres,
                "apellidos_denunciado": denuncia.denunciado.apellidos,
                "cedula_denunciado": denuncia.denunciado.cedula,
                "telefono_denunciado": denuncia.denunciado.telefono,
                "email_denunciado": denuncia.denunciado.email,
                "direccion_denunciado": denuncia.denunciado.direccion,
                "estatus": denuncia.estatus,
                "ente": denuncia.ente,
                "motivo": denuncia.motivo,
                "zona": denuncia.zona,
                "fecha_denuncia": denuncia.fecha_denuncia,
                "fecha_incidente": denuncia.fecha_incidente,
            }
        return {}


class DenunciaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "asesoria.denuncias.editar_denuncia"
    form_class = DenunciaForm

    def __init__(self):
        self.service = DenunciaService()
