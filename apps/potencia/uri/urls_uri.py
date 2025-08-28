from django.urls import include, path
from potencia.views import PotenciaView

urlpatterns = [
    path(
        "unidad-respuesta-inmediata/",
        include(("apps.potencia.uri.urls", "uri")),
    ),
    path(
        "api/unidad-respuesta-inmediata/",
        include(("apps.potencia.uri.urls_apis", "api_uri")),
    ),
]
