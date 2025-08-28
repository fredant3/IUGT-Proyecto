from organizacion.reglamentos.models import Reglamento
from helpers.FormBase import FormBase
from django import forms


class ReglamentoForm(FormBase):
    date = FormBase.create_date_field("date", title="Fecha de publicación")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields.pop("file")

    class Meta:
        model = Reglamento
        fields = [
            "name",
            "file",
            "date",
            "progre",
            "estado",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del reglamento",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Seleccione el archivo",
                    "accept": ".pdf",
                }
            ),
            "progre": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el progreso",
                }
            ),
            "estado": forms.Select(
                attrs={
                    "class": "form-select mb-3",
                    "placeholder": "Seleccione el estado",
                }
            ),
        }
