from administracion.departamentos.views.create_view import DepartamentoCreateApiView
from administracion.departamentos.views.delete_view import DepartamentoDeleteApiView
from administracion.departamentos.views.list_view import DepartamentoListApiView
from administracion.departamentos.views.update_view import DepartamentoUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        DepartamentoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DepartamentoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        DepartamentoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DepartamentoDeleteApiView.as_view(),
        name="delete",
    ),
]
