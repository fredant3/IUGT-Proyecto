from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    TextValidator,
    PhoneNumberValidator,
    CedulaVenezolanaValidator,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import (
    DateField,
    EmailField,
    CharField,
    ForeignKey,
    TextField,
    CASCADE,
)


ESTATUS_CHOICES = (
    ("reg", "Registrado"),
    ("pro", "En Proceso"),
    ("nop", "No Procede"),
)


class Denunciante(BaseModel):
    nombres = CharField(
        "Nombre del denunciante",
        max_length=120,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    apellidos = CharField(
        "Apellido del denunciante",
        max_length=120,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    cedula = CharField(
        "Cédula del denunciante",
        max_length=15,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    telefono = CharField(
        "Teléfono del denunciante",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    email = EmailField(
        "Correo electrónico del denunciante", max_length=60, blank=True, null=True
    )
    direccion = CharField(
        "Dirección del denunciante",
        max_length=180,
        validators=[MinLengthValidator(6), MaxLengthValidator(180), TextValidator()],
    )

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"

    class Meta:
        verbose_name = "Denunciante"
        verbose_name_plural = "Denunciantes"
        permissions = [
            ("listar_denunciante", "Puede listar denunciantes"),
            ("agregar_denunciante", "Puede agregar denunciante"),
            ("ver_denunciante", "Puede ver denunciante"),
            ("editar_denunciante", "Puede actualizar denunciante"),
            ("eliminar_denunciante", "Puede eliminar denunciante"),
        ]


class Denunciado(BaseModel):
    nombres = CharField(
        "Nombre del denunciado",
        max_length=120,
        blank=True,
        null=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    apellidos = CharField(
        "Apellido del denunciado",
        max_length=120,
        blank=True,
        null=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(120), TextValidator()],
    )
    cedula = CharField(
        "Cédula del denunciado",
        max_length=15,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(7),
            MaxLengthValidator(14),
            CedulaVenezolanaValidator(),
        ],
    )
    telefono = CharField(
        "Teléfono del denunciado",
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    email = EmailField(
        "Correo electrónico del denunciado", max_length=60, blank=True, null=True
    )
    direccion = CharField(
        "Dirección del denunciado",
        max_length=180,
        blank=True,
        null=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(180), TextValidator()],
    )

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Denunciado"
        verbose_name_plural = "Denunciados"
        permissions = [
            ("listar_denunciado", "Puede listar denunciados"),
            ("agregar_denunciado", "Puede agregar denunciado"),
            ("ver_denunciado", "Puede ver denunciado"),
            ("editar_denunciado", "Puede actualizar denunciado"),
            ("eliminar_denunciado", "Puede eliminar denunciado"),
        ]


class Denuncia(BaseModel):
    estatus = CharField(max_length=3, choices=ESTATUS_CHOICES)
    ente = CharField(
        "Ente Relacionado",
        max_length=50,
        blank=True,
        null=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(50), TextValidator()],
    )
    denunciante = ForeignKey(Denunciante, on_delete=CASCADE)
    denunciado = ForeignKey(Denunciado, on_delete=CASCADE)
    motivo = TextField(
        max_length=400,
        validators=[MinLengthValidator(6), MaxLengthValidator(400), TextValidator()],
    )
    zona = CharField(
        "Zona del Incidente",
        max_length=150,
        blank=True,
        null=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(150), TextValidator()],
    )
    fecha_denuncia = DateField("Fecha de la denuncia")
    fecha_incidente = DateField("Fecha del incidente", blank=True, null=True)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.ente

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"
        permissions = [
            ("listar_denuncia", "Puede listar denuncias"),
            ("agregar_denuncia", "Puede agregar denuncia"),
            ("ver_denuncia", "Puede ver denuncia"),
            ("editar_denuncia", "Puede actualizar denuncia"),
            ("eliminar_denuncia", "Puede eliminar denuncia"),
            ("exel_denuncia", "Puede exportar a exel denuncias"),
        ]
