from django.urls import include, path

urlpatterns = [
    path("", include(("apps.emergencia.urls_webs", "emergencias"))),
    path("api/", include(("apps.emergencia.urls_apis", "api_emergencias"))),
]
