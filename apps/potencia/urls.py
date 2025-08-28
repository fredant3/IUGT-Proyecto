from django.urls import include, path
from potencia.views import PotenciaView

urlpatterns = [
    path("", PotenciaView.as_view(), name="potencia"),
    path("incidencias/", include(("apps.potencia.incidencias.urls", "incidencias"))),
    path(
        "api/incidencias/",
        include(("apps.potencia.incidencias.urls_apis", "api_incidencias")),
    ),
    path(
        "tipoIncidencia/",
        include(("apps.potencia.tipo_incidencia.urls", "tipoIncidencia")),
    ),
    path(
        "api/tipoIncidencia/",
        include(("apps.potencia.tipo_incidencia.urls_apis", "api_tipoIncidencia")),
    ),
]
