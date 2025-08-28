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


class Normativa(BaseModel):
    name = CharField(
        "Nombre de Normativa",
        max_length=64,
        validators=[MinLengthValidator(3), MaxLengthValidator(64), TextValidator()],
    )
    file = FileField("Archivo", upload_to="normativas/", validators=[Validate_pdf])
    date = DateField("Fecha", blank=True)
    progre = CharField("Progreso:", max_length=3, choices=PROGRESS_CHOICES, default="0")
    estado = CharField("Estatus", max_length=3, choices=ESTATUS_CHOICES, default="bor")

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "normativa"
        verbose_name_plural = "normativas"
        permissions = [
            ("listar_normativa", "Puede listar normativas"),
            ("agregar_normativa", "Puede agregar normativa"),
            ("ver_normativa", "Puede ver normativa"),
            ("editar_normativa", "Puede actualizar normativa"),
            ("eliminar_normativa", "Puede eliminar normativa"),
        ]
