from django.utils import timezone
from django import forms
from helpers.FormBase import FormBase
from seguridad.vehiculos.models import Vehiculo
from helpers.validForm import validate_cedula, validate_decimal_number
from datetime import datetime


class VehiculoForm(FormBase):
    fecha = FormBase.create_date_field("fecha", title="Fecha de registro")
    hora = FormBase.create_time_field("hora", title="Hora de registro")

    class Meta:
        model = Vehiculo
        fields = (
            "nombre",
            "apellido",
            "cedula",
            "modelo",
            "vehiculo",
            "motivo",
            "cantigasolina",
            "capagasolina",
            "placa",
            "fecha",
            "hora",
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
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del conductor",
                }
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese los apellidos"}
            ),
            "cedula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: 12345678"}
            ),
            "modelo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Toyota Hilux 2023"}
            ),
            "vehiculo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tipo de vehiculo"}
            ),
            "motivo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describa el motivo del registro",
                    "rows": 3,
                }
            ),
            "capagasolina": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Capacidad del tanque (en litros)",
                }
            ),
            "cantigasolina": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 15.5 (en litros)",
                    "step": "0.1",
                    "min": "0",
                }
            ),
            "placa": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: ABC123"}
            ),
        }

    def clean_cedula(self):
        data = self.cleaned_data.get("cedula")
        validate_cedula(data, "Formato de cédula inválido. Use: V-12345678")
        return data

    def clean_cantigasolina(self):
        data = self.cleaned_data.get("cantigasolina")
        validate_decimal_number(
            str(data), "La cantidad de gasolina debe ser un número positivo (ej: 15.5)"
        )
        return data

    def clean_fecha(self):
        data = self.cleaned_data.get("fecha")
        if data and data > timezone.now().date():
            raise forms.ValidationError("La fecha no puede ser futura")
        return data

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get("fecha")
        hora = cleaned_data.get("hora")

        if fecha and hora:
            # Convertir a datetime con zona horaria
            registro_datetime = timezone.make_aware(
                datetime.combine(fecha, hora), timezone.get_current_timezone()
            )

            if registro_datetime > timezone.now():
                self.add_error("hora", "La combinación fecha/hora no puede ser futura")

        # Validación de gasolina
        cantigasolina = cleaned_data.get("cantigasolina", 0)
        if cantigasolina is not None and float(cantigasolina) <= 0:
            self.add_error(
                "cantigasolina",
                "Debe especificar una cantidad válida de gasolina (mayor a 0)",
            )

        return cleaned_data
