from helpers.FormBase import FormBase
from presupuesto.proyecto.models import Proyecto
from django import forms


class ProyectoForm(FormBase):
    fechai = FormBase.create_date_field("fechai", title="Fecha de inicio")
    fechac = FormBase.create_date_field("fechac", title="Fecha de culminacion")

    class Meta:
        model = Proyecto
        fields = (
            "nombrep",
            "fechai",
            "fechac",
            "situacionp",
            "montoproyecto",
            "responsableg",
            "responsablet",
            "responsabler",
            "responsablea",
            "estatus",
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
        labels = {
            "nombrep": "Nombre del Proyecto",
            "montoproyecto": "Monto del Proyecto",
            "situacionp": "Situación Actual",
        }
        widgets = {
            "nombrep": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del proyecto",
                }
            ),
            "responsableg": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable gerente",
                }
            ),
            "responsablet": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable tecnico",
                }
            ),
            "responsabler": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable registrador",
                }
            ),
            "responsablea": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable administrativo",
                }
            ),
            "estatus": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el estatus",
                }
            ),
            "situacionp": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la situación del proyecto",
                }
            ),
            "montoproyecto": forms.NumberInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el monto del proyecto",
                    "min": "0",
                    "step": "0.01",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        fechai = cleaned_data.get("fechai")
        fechac = cleaned_data.get("fechac")

        if fechai and fechac and fechac < fechai:
            self.add_error(
                "fechac",
                "La fecha de culminación no puede ser anterior a la fecha de inicio",
            )
        return cleaned_data
