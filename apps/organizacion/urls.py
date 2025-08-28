from django.urls import include, path

from organizacion.views import OrganizacionView

urlpatterns = [
    path("", OrganizacionView.as_view(), name="organizacion"),
    path(
        "reglamentos/", include(("apps.organizacion.reglamentos.urls", "reglamentos"))
    ),
    path(
        "api/reglamentos/",
        include(("apps.organizacion.reglamentos.urls_apis", "api_reglamentos")),
    ),
    path("normativas/", include(("apps.organizacion.normativas.urls", "normativas"))),
    path(
        "api/normativas/",
        include(("apps.organizacion.normativas.urls_apis", "api_normativas")),
    ),
]
