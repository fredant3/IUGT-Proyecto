from django.urls import path

from presupuesto.partida.views.create_view import PartidaCreateView
from presupuesto.partida.views.delete_view import PartidaDeleteView
from presupuesto.partida.views.list_view import PartidaListView
from presupuesto.partida.views.update_view import PartidaUpdateView


urlpatterns = [
    path(
        "",
        PartidaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        PartidaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        PartidaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        PartidaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        PartidaDeleteView.as_view(),
        name="delete",
    ),
]
