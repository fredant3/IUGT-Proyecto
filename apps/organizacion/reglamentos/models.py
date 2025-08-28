from django.db.models import (
    CharField,
    FileField,
    DateField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.validForm import TextValidator, Validate_pdf
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
)

PROGRESS_CHOICES = (
    ("0", "0%"),
    ("10", "10%"),
    ("20", "20%"),
    ("30", "30%"),
    ("40", "40%"),
    ("50", "50%"),
    ("60", "60%"),
    ("70", "70%"),
    ("80", "80%"),
    ("90", "90%"),
    ("100", "100%"),
)

ESTATUS_CHOICES = (("bor", "Borrador"), ("rev", "Revision"), ("pub", "Publicado"))


class Reglamento(BaseModel):
    name = CharField(
        "Nombre de Reglamento:",
        max_length=64,
        validators=[MinLengthValidator(3), MaxLengthValidator(64), TextValidator()],
    )
    file = FileField("Archivo", upload_to="reglamentos/", validators=[Validate_pdf])
    date = DateField("Fecha", blank=True)
    progre = CharField("Progreso:", max_length=64, choices=PROGRESS_CHOICES)
    estado = CharField("Estatus", max_length=3, choices=ESTATUS_CHOICES, default="bor")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "reglamento"
        verbose_name_plural = "reglamentos"
        permissions = [
            ("listar_reglamento", "Puede listar reglamentos"),
            ("agregar_reglamento", "Puede agregar reglamento"),
            ("ver_reglamento", "Puede ver reglamento"),
            ("editar_reglamento", "Puede actualizar reglamento"),
            ("eliminar_reglamento", "Puede eliminar reglamento"),
        ]
