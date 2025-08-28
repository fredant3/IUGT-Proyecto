from django.urls import include, path

from seguridad.views import SeguridadView

urlpatterns = [
    path(
        "",
        SeguridadView.as_view(),
        name="seguridad",
    ),
    path("entradas/", include(("apps.seguridad.entradas.urls", "entradas"))),
    path(
        "api/entradas/",
        include(("apps.seguridad.entradas.urls_apis", "api_entradas")),
    ),
    path("gestiones/", include(("apps.seguridad.gestiones.urls", "gestiones"))),
    path(
        "api/gestiones/",
        include(("apps.seguridad.gestiones.urls_apis", "api_gestiones")),
    ),
    path("salidas/", include(("apps.seguridad.salidas.urls", "salidas"))),
    path(
        "api/salidas/",
        include(("apps.seguridad.salidas.urls_apis", "api_salidas")),
    ),
    path(
        "vehiculos/",
        include(("apps.seguridad.vehiculos.urls", "vehiculos")),
    ),
    path(
        "api/vehiculos/",
        include(("apps.seguridad.vehiculos.urls_apis", "api_vehiculos")),
    ),
]
