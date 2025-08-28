from django import forms
from organizacion.normativas.models import Normativa
from helpers.FormBase import FormBase


class NormativaForm(FormBase):
    date = FormBase.create_date_field("date", "Fecha de publicación")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Normativa
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre de la normativa",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Seleccione el archivo",
                    "accept": ".pdf",
                }
            ),
        }
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
