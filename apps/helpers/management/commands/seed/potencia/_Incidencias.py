from potencia.incidencias.models import TipoIncidencia

TIPOS_DE_INCIDENCIAS = ["Averia", "Falla"]


class IncidenciaFake:
    def tipo_incidencia():
        for tipo_incidencia_model in TIPOS_DE_INCIDENCIAS:
            model = TipoIncidencia.objects.create(tipo=tipo_incidencia_model)
            print(f"Tipo Incidencia {model.tipo} registrado")
