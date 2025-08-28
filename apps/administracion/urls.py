from administracion.views import AdministracionView
from django.urls import include, path

urlpatterns = [
    path("", AdministracionView.as_view(), name="administracion"),
    path(
        "asignaciones/",
        include(("apps.administracion.asignaciones.urls", "asignaciones")),
    ),
    path(
        "api/asignaciones/",
        include(("apps.administracion.asignaciones.urls_apis", "api_asignaciones")),
    ),
    path(
        "averias/",
        include(("apps.administracion.averia.urls", "averias")),
    ),
    path(
        "api/averias/",
        include(("apps.administracion.averia.urls_apis", "api_averias")),
    ),
    path(
        "compras/",
        include(("apps.administracion.compras.urls", "compras")),
    ),
    path(
        "api/compras/",
        include(("apps.administracion.compras.urls_apis", "api_compras")),
    ),
    path(
        "departamentos/",
        include(("apps.administracion.departamentos.urls", "departamentos")),
    ),
    path(
        "api/departamentos/",
        include(("apps.administracion.departamentos.urls_apis", "api_departamentos")),
    ),
    path(
        "articulos/",
        include(("apps.administracion.inventario.urls", "articulos")),
    ),
    path(
        "api/articulos/",
        include(("apps.administracion.inventario.urls_apis", "api_articulos")),
    ),
    path(
        "sedes/",
        include(("apps.administracion.sedes.urls", "sedes")),
    ),
    path(
        "api/sedes/",
        include(("apps.administracion.sedes.urls_apis", "api_sedes")),
    ),
    path(
        "tipo_averia/",
        include(("apps.administracion.tipo_averia.urls", "tipo_averias")),
    ),
    path(
        "api/tipo_averia/",
        include(("apps.administracion.tipo_averia.urls_apis", "api_tipo_averias")),
    ),
]