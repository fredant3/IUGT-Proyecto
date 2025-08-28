from django.urls import path

from seguridad.entradas.views.create_view import EntradaCreateApiView
from seguridad.entradas.views.delete_view import EntradaDeleteApiView
from seguridad.entradas.views.list_view import EntradaListApiView
from seguridad.entradas.views.update_view import EntradaUpdateApiView

urlpatterns = [
    path(
        "",
        EntradaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EntradaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EntradaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EntradaDeleteApiView.as_view(),
        name="delete",
    ),
]
