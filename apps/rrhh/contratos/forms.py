from rrhh.contratos.models import Contrato
from helpers.FormBase import FormBase


class ContratoForm(FormBase):
    fecha_ingreso_911 = FormBase.create_date_field(
        "fecha_ingreso_911", title="Fecha Ingreso 911"
    )
    fecha_ingreso_apn = FormBase.create_date_field(
        "fecha_ingreso_apn", title="Fecha Ingreso APN"
    )
    fecha_ingreso = FormBase.create_date_field("fecha_ingreso", title="Fecha Ingreso")
    fecha_culminacion = FormBase.create_date_field(
        "fecha_culminacion", title="Fecha Culminacion"
    )

    class Meta:
        model = Contrato
        fields = (
            "tipo",
            "comision_servicio",
            "pnb",
            "departamento",
            "cargo",
            "sede",
            "fecha_ingreso_911",
            "fecha_ingreso_apn",
            "fecha_ingreso",
            "fecha_culminacion",
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
            "tipo": "Tipo de contrato",
            "cargo": "Cargo asignado",
            "empleado": "Nombre del empleado",
        }
        widgets = {}

    # Validación de fechas
    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get("fecha_ingreso")
        fecha_culminacion = cleaned_data.get("fecha_culminacion")

        if fecha_ingreso and fecha_culminacion:
            if fecha_culminacion < fecha_ingreso:
                self.add_error(
                    "fecha_culminacion",
                    "La fecha de culminación no puede ser anterior a la fecha de ingreso",
                )

        # Validación adicional para fecha_ingreso_911 y fecha_ingreso_apn
        fecha_911 = cleaned_data.get("fecha_ingreso_911")
        fecha_apn = cleaned_data.get("fecha_ingreso_apn")

        if fecha_911 and fecha_apn and fecha_apn < fecha_911:
            self.add_error(
                "fecha_ingreso_apn",
                "La fecha de ingreso APN no puede ser anterior al ingreso 911",
            )

        return cleaned_data
