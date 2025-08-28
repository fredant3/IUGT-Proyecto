from administracion.departamentos.models import Departamento
from administracion.sedes.models import Sede
from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel


class TipoIncidencia(BaseModel):
    tipo = models.CharField(max_length=120)

    def __str__(self):
        return self.tipo


class Incidencia(BaseModel):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.CharField("Estado", max_length=120)
    tipo_incidencia = models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    tipo_solicitud = models.CharField(max_length=80, verbose_name="Tipo Solicitud")
    observaciones = models.CharField(max_length=200)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
