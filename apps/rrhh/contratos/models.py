from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db.models import CASCADE, CharField, DateField, ForeignKey, BooleanField
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from rrhh.cargos.models import Cargo
from rrhh.empleados.models import Empleado
from helpers.models import BOOLEAN_CHOICES

TIPO_CONTRATOS_CHOICES = (
    ("pasante", "Pasante"),
    ("prueba", "Periodo de Prueba"),
    ("contrato", "Contratado"),
    ("fijo", "Personal Fijo"),
)

ESTATUS_CONTRATO_CHOICES = (
    ("act", "Activo"),
    ("pen", "Pendiente de Inicio"),
    ("sus", "Suspendido"),
    ("ter", "Terminado"),
    ("ren", "Renuncia Voluntaria"),
    ("des", "Despido"),
    ("fin", "Finalizado por Término de Contrato"),
    ("inc", "Incapacitado"),
    ("lic", "En Licencia"),
    ("vac", "En Vacaciones"),
    ("aju", "Ajuste de Contrato"),
    ("ces", "Cesado"),
    ("ret", "Jubilado/Retirado"),
    ("fal", "Fallecido"),
)


class Contrato(BaseModel):
    tipo = CharField("Tipo de contrato", max_length=8, choices=TIPO_CONTRATOS_CHOICES)
    comision_servicio = BooleanField(
        "Comision servicio",
        choices=BOOLEAN_CHOICES,
        default=BOOLEAN_CHOICES[1],
    )
    pnb = BooleanField(
        "Funcionario PNB",
        choices=BOOLEAN_CHOICES,
        default=BOOLEAN_CHOICES[1],
    )
    departamento = ForeignKey(
        Departamento, on_delete=CASCADE, verbose_name="Departamento"
    )
    cargo = ForeignKey(Cargo, on_delete=CASCADE, verbose_name="Cargo asignado")
    sede = ForeignKey(Sede, on_delete=CASCADE, verbose_name="Sede")
    fecha_ingreso_911 = DateField("Fecha de ingreso al Ven-911")
    fecha_ingreso_apn = DateField("Fecha de ingreso APN")
    # fasmij = BooleanField(choices=BOOLEAN_CHOICES,default=BOOLEAN_CHOICES[1],)
    fecha_ingreso = DateField("Fecha de ingreso")
    fecha_culminacion = DateField("Fecha de culminacion", null=True, blank=True)
    estatus = CharField(max_length=3, choices=ESTATUS_CONTRATO_CHOICES, default="pen")
    empleado = ForeignKey(
        Empleado,
        on_delete=CASCADE,
        verbose_name="Nombre del empleado",
        related_name="contratos",
    )

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.empleado.nombres, self.empleado.apellidos)

    class Meta:
        verbose_name = "contrato"
        verbose_name_plural = "contratos"
        permissions = [
            ("listar_contrato", "Puede listar contratos"),
            ("agregar_contrato", "Puede agregar contrato"),
            ("ver_contrato", "Puede ver contrato"),
            ("editar_contrato", "Puede actualizar contrato"),
            ("eliminar_contrato", "Puede eliminar contrato"),
            ("exel_contrato", "Puede exportar contrato a excel"),
        ]
