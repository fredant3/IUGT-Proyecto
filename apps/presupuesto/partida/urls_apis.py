from django.urls import path

from presupuesto.partida.views.create_view import PartidaCreateApiView
from presupuesto.partida.views.delete_view import PartidaDeleteApiView
from presupuesto.partida.views.list_view import PartidaListApiView
from presupuesto.partida.views.update_view import PartidaUpdateApiView


urlpatterns = [
    path(
        "",
        PartidaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        PartidaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        PartidaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        PartidaDeleteApiView.as_view(),
        name="delete",
    ),
]
