from django.urls import include, path
from asesoria.views import AsesoriaView

urlpatterns = [
    path("", AsesoriaView.as_view(), name="asesoria"),
    path("denuncias/", include(("apps.asesoria.denuncias.urls", "denuncias"))),
    path(
        "api/denuncias/",
        include(("apps.asesoria.denuncias.urls_apis", "api_denuncias")),
    ),
    path("registros-filmicos/", include(("apps.asesoria.filmicos.urls", "filmicos"))),
    path(
        "api/registros-filmicos/",
        include(("apps.asesoria.filmicos.urls_apis", "api_filmicos")),
    ),
]
