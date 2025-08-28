from django import forms
from presupuesto.models import Accion
from helpers.FormBase import FormBase


class AccionForm(FormBase):
    fecha_inicio = FormBase.create_date_field("fecha_inicio", title="Fecha Inicio")
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", title="Fecha Culminacion"
    )

    class Meta:
        model = Accion
        fields = (
            "proyecto_acciones",
            "fecha_inicio",
            "fecha_culminacion",
            "situacion_presupuestaria",
            "monto",
            "responsable_gerente",
            "responsable_tecnico",
            "responsable_registrador",
            "responsable_administrativo",
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
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control datepicker"}),
            "fecha_culminacion": forms.DateInput(
                attrs={"class": "form-control datepicker"}
            ),
            "responsable_gerente": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable gerente",
                }
            ),
            "responsable_tecnico": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable tecnico",
                }
            ),
            "responsable_registrador": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese el nombre del responsable registrador",
                }
            ),
            "responsable_administrativo": forms.TextInput(
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
            "monto": forms.TextInput(
                attrs={"placeholder": "Ej: Bs. 1.234,56 / $1,234.56 / 1.234,56 €"}
            ),
            "situacion_presupuestaria": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ingrese la situacion presupuestaria",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_inicio and fecha_culminacion:
            if fecha_culminacion < fecha_inicio:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de inicio",
                )

        return cleaned_data
