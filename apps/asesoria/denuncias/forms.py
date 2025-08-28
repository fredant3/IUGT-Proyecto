from asesoria.denuncias.models import Denuncia
from django.forms import TextInput, CharField, EmailField, EmailInput
from django.core.validators import MinLengthValidator, MaxLengthValidator
from helpers.FormBase import FormBase
from helpers.validForm import (
    TextValidator,
    PhoneNumberValidator,
    CedulaVenezolanaValidator,
    validate_email,
)


class DenunciaForm(FormBase):
    nombres_denunciante = CharField(
        label="Nombre del Denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese el nombre del denunciante"}),
        max_length=120,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    apellidos_denunciante = CharField(
        label="Apellido Del Denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese el apellido del denunciante"}),
        max_length=120,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    cedula_denunciante = CharField(
        label="Cédula del Denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese la cédula del denunciante"}),
        max_length=15,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    telefono_denunciante = CharField(
        label="Teléfono del Denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese el teléfono del denunciante"}),
        max_length=20,
        required=False,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    email_denunciante = EmailField(
        label="Correo electrónico del Denunciante",
        widget=EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciante"}
        ),
        max_length=60,
        required=False,
        validators=[validate_email],
    )
    direccion_denunciante = CharField(
        label="Dirección del Denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese la dirección del denunciante"}),
        max_length=180,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )

    nombres_denunciado = CharField(
        label="Nombre del Denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese el nombre del denunciado"}),
        max_length=120,
        required=False,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    apellidos_denunciado = CharField(
        label="Apellido del Denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese el apellido del denunciado"}),
        max_length=120,
        required=False,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    cedula_denunciado = CharField(
        label="Cédula del Denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese la cédula del denunciado"}),
        max_length=15,
        required=False,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    telefono_denunciado = CharField(
        label="Teléfono del Denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese el teléfono del denunciado"}),
        max_length=20,
        required=False,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    email_denunciado = EmailField(
        label="Correo electrónico del Denunciado",
        widget=EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciado"}
        ),
        max_length=60,
        required=False,
        validators=[validate_email],
    )
    direccion_denunciado = CharField(
        label="Dirección del Denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese la dirección del denunciado"}),
        max_length=180,
        required=False,
        validators=[MinLengthValidator(4), MaxLengthValidator(180), TextValidator()],
    )
    fecha_denuncia = FormBase.create_date_field("fecha_denuncia")
    fecha_incidente = FormBase.create_date_field("fecha_incidente")

    class Meta:
        model = Denuncia
        fields = [
            "nombres_denunciante",
            "apellidos_denunciante",
            "cedula_denunciante",
            "telefono_denunciante",
            "email_denunciante",
            "direccion_denunciante",
            "nombres_denunciado",
            "apellidos_denunciado",
            "cedula_denunciado",
            "telefono_denunciado",
            "email_denunciado",
            "direccion_denunciado",
            "estatus",
            "ente",
            "motivo",
            "zona",
            "fecha_denuncia",
            "fecha_incidente",
        ]
        widgets = {
            "ente": TextInput(attrs={"placeholder": "Ingrese el ente relacionado"}),
            "zona": TextInput(attrs={"placeholder": "Ingrese la zona del incidente"}),
            "motivo": TextInput(
                attrs={"placeholder": "Ingrese el motivo de la denuncia"}
            ),
        }
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
