from administracion.inventario.views.create_view import ArtiluloCreateApiView
from administracion.inventario.views.delete_view import ArticuloDeleteApiView
from administracion.inventario.views.list_view import ArticuloListApiView
from administracion.inventario.views.update_view import ArticuloUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        ArticuloListApiView.as_view(),
        name="list",
    ),
    path(
        "create/<str:type>/",
        ArtiluloCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ArticuloUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ArticuloDeleteApiView.as_view(),
        name="delete",
    ),
]
