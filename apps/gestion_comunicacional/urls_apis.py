from django.urls import path
from gestion_comunicacional.views.create_view import GestioncomunicacoinalCreateApiView
from gestion_comunicacional.views.delete_view import GestioncomunicacionalDeleteApiView
from gestion_comunicacional.views.list_view import GestioncomunicacionalListApiView
from gestion_comunicacional.views.update_view import GestioncomunicacionalUpdateApiView

urlpatterns = [
    path(
        "",
        GestioncomunicacionalListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        GestioncomunicacoinalCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        GestioncomunicacionalUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        GestioncomunicacionalDeleteApiView.as_view(),
        name="delete",
    ),
]
