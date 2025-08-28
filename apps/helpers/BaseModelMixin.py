from datetime import datetime
from django.db import models
from django.utils.timezone import get_current_timezone

ESTADOS_CHOICES = (
    ("1", "Amazonas"),
    ("2", "Anzoátegui"),
    ("3", "Apure"),
    ("4", "Aragua"),
    ("5", "Barinas"),
    ("6", "Bolívar"),
    ("7", "Carabobo"),
    ("8", "Cojedes"),
    ("9", "Delta Amacuro"),
    ("10", "Falcón"),
    ("11", "Guárico"),
    ("12", "Lara"),
    ("13", "Mérida"),
    ("14", "Miranda"),
    ("15", "Monagas"),
    ("16", "Nueva Esparta"),
    ("17", "Portuguesa"),
    ("18", "Sucre"),
    ("19", "Táchira"),
    ("20", "Trujillo"),
    ("21", "Vargas"),
    ("22", "Yaracuy"),
    ("23", "Zulia"),
    ("24", "Distrito Capital"),
)

ESTATUS_CHOICES = (("activo", "Activo"), ("inactivo", "Inactivo"))
YES_NO_CHOICES = (("si", "Si"), ("no", "No"))
MONTH_CHOICES = (
    ("ene", "Enero"),
    ("feb", "Febrero"),
    ("mar", "Marzo"),
    ("abr", "Abril"),
    ("may", "Mayo"),
    ("jun", "Junio"),
    ("jul", "Julio"),
    ("ago", "Agosto"),
    ("sep", "Septiembre"),
    ("oct", "Octubre"),
    ("nov", "Noviembre"),
    ("dic", "Diciembre"),
)

DEP_AVERIA = (
    ("1", "Asesoría Jurídica"),
    ("2", "Gestión Humana"),
    ("3", "Gestión Administrativa"),
    ("4", "Unidad de Respuesta Inmediata"),
    ("5", "Potencia"),
    ("6", "Organización"),
    ("7", "Presupuestos"),
    ("8", "Planificación"),
    ("9", "Protección y Seguridad Integral"),
    ("10", "Biblioteca de Manuales"),
    ("11", "Operaciones"),
    ("12", "Tecnología Comunicación e Información"),
    ("13", "Gestion Comunicacional"),
)


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(deleted_at__isnull=False)

    def all_with_deleted(self):
        return super().get_queryset()


class BaseModel(models.Model):
    created_by = models.CharField(verbose_name="Creado por", max_length=6)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_by = models.CharField(verbose_name="Actualizado por", max_length=6)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    deleted_by = models.CharField(
        verbose_name="Eliminado por", max_length=6, null=True, blank=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="Eliminado el", null=True, blank=True
    )

    objects = BaseModelManager()

    def delete(self):
        self.deleted_at = datetime.now(tz=get_current_timezone())
        self.save()

    def hard_delete(self):
        return super().delete()

    class Meta:
        abstract = True
