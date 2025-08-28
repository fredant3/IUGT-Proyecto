from django.urls import include, path

urlpatterns = [
    path("incidencias/", include(("apps.potencia.incidencias.urls", "incidencias"))),
    path(
        "api/incidencias/",
        include(("apps.potencia.incidencias.urls_apis", "api_incidencias")),
    ),
]
