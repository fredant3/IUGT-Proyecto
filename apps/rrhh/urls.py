from django.urls import include, path
from apps.rrhh.views import GestionHumanaView

urlpatterns = [
    path("", GestionHumanaView.as_view(), name="gestion_humana"),
    path("cargos/", include(("apps.rrhh.cargos.urls", "cargos"))),
    path(
        "api/cargos/",
        include(("apps.rrhh.cargos.urls_apis", "api_cargos")),
    ),
    path("sueldos/tipos", include(("apps.rrhh.tipos_sueldos.urls", "tipos_sueldos"))),
    path(
        "api/sueldos/tipos/",
        include(("apps.rrhh.tipos_sueldos.urls_apis", "api_tipos_sueldos")),
    ),
    path("contratos/", include(("apps.rrhh.contratos.urls", "contratos"))),
    path(
        "api/contratos/",
        include(("apps.rrhh.contratos.urls_apis", "api_contratos")),
    ),
]
