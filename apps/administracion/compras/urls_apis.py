from administracion.compras.views.create_view import CompraCreateApiView
from administracion.compras.views.delete_view import CompraDeleteApiView
from administracion.compras.views.list_view import CompraListApiView
from administracion.compras.views.update_view import ComprasUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        CompraListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CompraCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ComprasUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CompraDeleteApiView.as_view(),
        name="delete",
    ),
]
