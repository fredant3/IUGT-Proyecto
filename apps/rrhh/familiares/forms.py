from django.forms import ValidationError, TextInput, Textarea
from rrhh.familiares.models import Familiar
from helpers.FormBase import FormBase
from django.utils import timezone


class FamiliarForm(FormBase):
    fecha_nacimiento = FormBase.create_date_field(
        "fecha_nacimiento",
        "Fecha de nacimiento",
    )

    class Meta:
        model = Familiar
        fields = (
            "parentezco",
            "tipo_hijo",
            "discapacidad",
            "nombres",
            "apellidos",
            "cedula",
            "fecha_nacimiento",
            "sexo",
            "estado_civil",
            "observacion",
        )
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
            "nombres": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese nombres completos",
                }
            ),
            "apellidos": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese apellidos completos",
                }
            ),
            "observacion": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese observaciones relevantes",
                    "rows": 3,
                }
            ),
        }

    def clean_fecha_nacimiento(self):
        data = self.cleaned_data.get("fecha_nacimiento")
        if data and data > timezone.now().date():
            raise ValidationError("La fecha de nacimiento no puede ser futura")
        return data

    def clean(self):
        cleaned_data = super().clean()
        discapacidad = cleaned_data.get("discapacidad")
        observacion = cleaned_data.get("observacion", "")

        if discapacidad == "si" and not observacion:
            self.add_error(
                "observacion",
                "Debe agregar una observación cuando existe una discapacidad",
            )

        return cleaned_data
