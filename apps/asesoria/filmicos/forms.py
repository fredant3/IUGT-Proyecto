from asesoria.filmicos.models import RegistroFilmico
from helpers.FormBase import FormBase
from django.forms import TextInput


class RegistroFilmicoForm(FormBase):
    fecha_solicitud = FormBase.create_date_field(
        "fecha_solicitud", "Fecha de Solicitud"
    )
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", "Fecha de Culminación"
    )

    class Meta:
        model = RegistroFilmico
        fields = [
            "estatus",
            "direccion",
            "camara",
            "motivo_solicitud",
            "ente_solicita",
            "fecha_solicitud",
            "fecha_culminacion",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "direccion": TextInput(attrs={"placeholder": "Ingrese la dirección"}),
            "camara": TextInput(attrs={"placeholder": "Ingrese la cámara"}),
            "motivo_solicitud": TextInput(
                attrs={"placeholder": "Ingrese el motivo de la solicitud"}
            ),
            "ente_solicita": TextInput(
                attrs={"placeholder": "Ingrese el ente que solicita"}
            ),
        }
