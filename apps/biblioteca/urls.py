from django.urls import path, include

from biblioteca.views import BibliotecatView

urlpatterns = [
    path(
        "",
        BibliotecatView.as_view(),
        name="bibliotecas",
    ),
    path(
        "normativas/",
        include(("apps.biblioteca.normativas.urls", "biblioteca_normativas")),
    ),
    path(
        "api/normativas/",
        include(("apps.biblioteca.normativas.urls_apis", "api_biblioteca_normativas")),
    ),
    path(
        "reglamentos/",
        include(("apps.biblioteca.reglamentos.urls", "biblioteca_reglamentos")),
    ),
    path(
        "api/reglamentos/",
        include(
            ("apps.biblioteca.reglamentos.urls_apis", "api_biblioteca_reglamentos")
        ),
    ),
]
