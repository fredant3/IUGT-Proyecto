from django.urls import include, path
from emergencia.views import EmergenciaView

urlpatterns = [
    path("", EmergenciaView.as_view(), name="operaciones"),
    # Rutas para operaciones
    path(
        "operaciones/",
        include(("apps.emergencia.operaciones.urls_webs", "operaciones")),
    ),
    path(
        "api/operaciones/",
        include(("apps.emergencia.operaciones.urls_apis", "api_operaciones")),
    ),
    # Rutas para incidencias
    path(
        "incidencias/",
        include(("apps.emergencia.incidencias.urls_webs", "operaciones_incidencias")),
    ),
    path(
        "api/incidencias/",
        include(
            ("apps.emergencia.incidencias.urls_apis", "api_operaciones_incidencias")
        ),
    ),
    # Rutas para organismo
        path(
        "organismo/",
        include(("apps.emergencia.organismo.urls_webs", "organismo")),
    ),
    path(
        "api/organismo/",
        include(
            ("apps.emergencia.organismo.urls_apis", "api_organismo")
        ),
    ),
]
