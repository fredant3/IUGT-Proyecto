from emergencia.incidencias.models import TipoIncidencia
from emergencia.organismo.models import Organismo


TIPOS_DE_INCIDENCIAS = ["Robo", "Asesinato", "Violencia", "Estafa"]
TIPOS_DE_ORGANISMO = ["CICPC", "Bomberos", "Policia Nacional", "SEBIN"]


class EmergenciaFake:
    def tipo_incidencia():
        for tipo_incidencia_model in TIPOS_DE_INCIDENCIAS:
            model = TipoIncidencia.objects.create(
                nombre_incidencia=tipo_incidencia_model
            )
            print(f"Tipo Incidencia {model.nombre_incidencia} registrado")

    def organismo():
        for field in TIPOS_DE_ORGANISMO:
            model = Organismo.objects.create(nombre=field)
            print(f"Tipo Incidencia {model.nombre} registrado")
