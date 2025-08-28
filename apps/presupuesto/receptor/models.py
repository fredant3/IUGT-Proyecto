from django.db.models import CharField, ForeignKey, CASCADE
from django.forms import model_to_dict
from presupuesto.partida.models import Partida
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    CurrencyValidator,
    TextValidator,
)
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)
from presupuesto.cedente.models import Cedente


class Receptor(BaseModel):
    cedente = ForeignKey(Cedente, on_delete=CASCADE, null=True)
    partida = ForeignKey(Partida, on_delete=CASCADE, null=True)

    denomr = CharField(
        "Denomincación",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    presuacorr = CharField(
        "Presupuesto acordado",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    caufechar = CharField(
        "Causado a la fecha",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )
    dispr = CharField(
        "Disponible a causar",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    montocr = CharField(
        "Monto a ceder",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    saldofr = CharField(
        "Saldo final",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    direccionr = CharField(
        "Dirección receptor",
        max_length=64,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(64),
            TextValidator(),
        ],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.generalr

    class Meta:
        verbose_name = "Receptor"
        verbose_name_plural = "Receptores"
        permissions = [
            ("listar_receptor", "Puede listar receptor"),
            ("agregar_receptor", "Puede agregar receptor"),
            ("ver_receptor", "Puede ver receptor"),
            ("editar_receptor", "Puede actualizar receptor"),
            ("eliminar_receptor", "Puede eliminar receptor"),
            ("pdf_receptor", "Puede generar pdf de receptor"),
        ]
