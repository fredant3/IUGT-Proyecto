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
    path("gestion-humana/", include(("apps.rrhh.urls"))),
    path("tecnologia/", include(("apps.tecnologia.urls"))),
    path("", RedirectView.as_view(url="dashboard", permanent=True)),
]
