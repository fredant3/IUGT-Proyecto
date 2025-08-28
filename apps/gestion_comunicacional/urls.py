from django.urls import path, include

from gestion_comunicacional.info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc_info"),
    path(
        "gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_webs", "gestioncomunicacional")),
    ),
    path(
        "api/gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_apis", "api_gestioncomunicacional")),
    ),
    path(
        "frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frente_preventivo.urls_webs",
                "frentepreventivo",
            )
        ),
    ),
    path(
        "api/frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frente_preventivo.urls_apis",
                "api_frentepreventivo",
            )
        ),
    ),
]
