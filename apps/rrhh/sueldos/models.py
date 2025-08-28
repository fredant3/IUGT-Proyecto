from django.db.models import (
    CharField,
    DateField,
    ForeignKey,
    CASCADE,
    DecimalField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.empleados.models import Empleado
from rrhh.tipos_sueldos.models import TipoSueldo

ESTATUS_CHOICES = (
    ("pendiente", "Por Pagar"),
    ("pagado", "Pago completado"),
    ("suspendido", "Suspendido"),
)


class Sueldo(BaseModel):
    tipo_sueldo = ForeignKey(TipoSueldo, on_delete=CASCADE)
    estatus = CharField(max_length=10, choices=ESTATUS_CHOICES)
    fecha_pago = DateField()
    monto = DecimalField(max_digits=10, decimal_places=2)
    empleado = ForeignKey(Empleado, on_delete=CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "sueldo"
        verbose_name_plural = "sueldos"
        permissions = [
            ("listar_sueldos", "Listar sueldos"),
            ("agregar_sueldo", "Agregar sueldos"),
            ("ver_sueldo", "Ver sueldos"),
            ("modificar_sueldo", "Modificar sueldos"),
            ("eliminar_sueldo", "Eliminar sueldos"),
            ("exel_sueldo", "Exportar sueldos a excel"),
        ]


class SueldoEmpleado(BaseModel):
    sueldo = ForeignKey(Sueldo, on_delete=CASCADE)
    fecha_pago = DateField()
    monto = DecimalField(max_digits=10, decimal_places=2)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "detalles del sueldo"
        verbose_name_plural = "destalles de los sueldos"
        permissions = [
            ("listar_sueldos", "Listar sueldos"),
            ("agregar_sueldo", "Agregar sueldos"),
            ("ver_sueldo", "Ver sueldos"),
            ("modificar_sueldo", "Modificar sueldos"),
            ("eliminar_sueldo", "Eliminar sueldos"),
            ("exel_sueldo", "Exportar sueldos a excel"),
        ]
