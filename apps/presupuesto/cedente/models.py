from django.db.models import CharField, ForeignKey, CASCADE
from django.forms import model_to_dict
from presupuesto.partida.models import Partida
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import (
    CurrencyValidator,
    TextValidator,
)
from django.core.validators import MinLengthValidator


class Cedente(BaseModel):

    partida = ForeignKey(Partida, on_delete=CASCADE, null=True)

    denomc = CharField(
        "Denominación",
        max_length=64,
        validators=[MinLengthValidator(4), TextValidator()],
    )
    presuacorc = CharField(
        "Presupuesto asignado",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    caufechac = CharField("Causado a la fecha", max_length=64)
    dispc = CharField("Disponible a causar", max_length=64)
    montocc = CharField(
        "Monto comprometido",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    saldofc = CharField(
        "Saldo final",
        max_length=64,
        validators=[CurrencyValidator()],
    )
    direccionc = CharField(
        "Dirección cedente",
        max_length=64,
        validators=[MinLengthValidator(4), TextValidator()],
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.generalc

    class Meta:
        verbose_name = "Cedente"
        verbose_name_plural = "Cedentes"
        permissions = [
            ("listar_cedente", "Puede listar cedente"),
            ("agregar_cedente", "Puede agregar cedente"),
            ("ver_cedente", "Puede ver cedente"),
            ("editar_cedente", "Puede actualizar cedente"),
            ("eliminar_cedente", "Puede eliminar cedente"),
            ("pdf_cedente", "Puede generar pdf de cedente"),
        ]
