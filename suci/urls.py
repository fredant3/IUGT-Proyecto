from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("", include(("apps.users.auth.urls", "auth"))),
    path("api/auth/", include(("apps.users.auth.urls_apis", "api_auth"))),
    path("dashboard/", include(("apps.dashboard.modules.urls", "modules"))),
    path("gestion-administrativa/", include(("apps.administracion.urls"))),
    path("asesoria-juridica/", include(("apps.asesoria.urls"))),
    path("biblioteca/", include(("apps.biblioteca.urls"))),
    path("organizacion/", include(("apps.organizacion.urls"))),
    path("operaciones/", include("apps.emergencia.urls")),
    path("planificacion/", include(("apps.planificacion.urls"))),
    path("presupuesto/", include(("apps.presupuesto.urls"))),
    path("potencia/", include(("apps.potencia.urls"))),
    path("uri/", include(("apps.potencia.uri.urls_uri"))),
    path("gestion-humana/", include(("apps.rrhh.urls"))),
    path("gestion-comunicacional/", include(("apps.gestion_comunicacional.urls"))),
    path("seguridad/", include(("apps.seguridad.urls"))),
    path("tecnologia/", include(("apps.tecnologia.urls"))),
    path("reporte_averia/", include(("apps.reporte_averia.urls", "reporte_averia"))),
    path("", RedirectView.as_view(url="dashboard", permanent=True)),
]
