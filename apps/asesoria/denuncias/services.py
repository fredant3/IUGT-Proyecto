from django.db.models import Q
from asesoria.denuncias.repositories import (
    DenunciadoRepository,
    DenuncianteRepository,
    DenunciaRepository,
)
from helpers.CrudMixin import CrudService


class DenunciaService(CrudService):
    denunciante_fields = [
        ("nombres", "nombres_denunciante"),
        ("apellidos", "apellidos_denunciante"),
        ("cedula", "cedula_denunciante"),
        ("telefono", "telefono_denunciante"),
        ("email", "email_denunciante"),
        ("direccion", "direccion_denunciante"),
    ]
    denunciado_fields = [
        ("nombres", "nombres_denunciado"),
        ("apellidos", "apellidos_denunciado"),
        ("cedula", "cedula_denunciado"),
        ("telefono", "telefono_denunciado"),
        ("email", "email_denunciado"),
        ("direccion", "direccion_denunciado"),
    ]

    def __init__(self):
        self.repository_denunciante = DenuncianteRepository()
        self.repository_denunciado = DenunciadoRepository()
        self.repository = DenunciaRepository()

    def create_denunciante(self, data):
        payload = self.change_key_create(self.denunciante_fields, data)
        return self.repository_denunciante.create(payload)

    def create_denunciado(self, data):
        payload = self.change_key_create(self.denunciado_fields, data)
        return self.repository_denunciado.create(payload)

    def before_create(self, data):
        payload = {}
        payload["estatus"] = data["estatus"]
        payload["ente"] = data["ente"]
        payload["motivo"] = data["motivo"]
        payload["zona"] = data["zona"]
        payload["fecha_denuncia"] = data["fecha_denuncia"]
        payload["fecha_incidente"] = data["fecha_incidente"]

        payload["denunciante"] = self.create_denunciante(data)
        payload["denunciado"] = self.create_denunciado(data)

        return payload

    def update_denunciante(self, entity, form_data):
        data = self.change_key_update(self.denunciante_fields, form_data)
        return self.repository_denunciante.update(entity, data)

    def update_denunciado(self, entity, form_data):
        data = self.change_key_update(self.denunciado_fields, form_data)
        return self.repository_denunciado.update(entity, data)

    def before_update(self, entity, form):
        # Actualizar denunciante
        self.update_denunciante(entity.denunciante, form.cleaned_data)

        # Actualizar denunciado
        denunciado_data = {
            "nombres": form.cleaned_data.get("nombres_denunciado"),
            "apellidos": form.cleaned_data.get("apellidos_denunciado"),
            "cedula": form.cleaned_data.get("cedula_denunciado"),
            "telefono": form.cleaned_data.get("telefono_denunciado"),
            "email": form.cleaned_data.get("email_denunciado"),
            "direccion": form.cleaned_data.get("direccion_denunciado"),
        }

        # Solo actualizar si hay datos para el denunciado
        if any(denunciado_data.values()):
            self.update_denunciado(entity.denunciado, form.cleaned_data)

        # Actualizar campos directos de la denuncia
        entity.estatus = form.cleaned_data.get("estatus", entity.estatus)
        entity.ente = form.cleaned_data.get("ente", entity.ente)
        entity.motivo = form.cleaned_data.get("motivo", entity.motivo)
        entity.zona = form.cleaned_data.get("zona", entity.zona)
        entity.fecha_denuncia = form.cleaned_data.get(
            "fecha_denuncia", entity.fecha_denuncia
        )
        entity.fecha_incidente = form.cleaned_data.get(
            "fecha_incidente", entity.fecha_incidente
        )
        entity.save()

    def criteria(self, search, arg=None):
        query = Q()

        if search:
            query &= (
                Q(denunciante__nombres__icontains=search)
                | Q(denunciante__apellidos__icontains=search)
                | Q(denunciante__cedula__icontains=search)
                | Q(denunciado__nombres__icontains=search)
                | Q(denunciado__apellidos__icontains=search)
                | Q(denunciado__cedula__icontains=search)
                | Q(zona__icontains=search)
            )

        return query
