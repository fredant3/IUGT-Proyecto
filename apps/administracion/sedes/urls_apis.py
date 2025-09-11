from administracion.sedes.views.create_view import SedeCreateApiView
from administracion.sedes.views.delete_view import SedeDeleteApiView
from administracion.sedes.views.list_view import SedeListApiView
from administracion.sedes.views.update_view import SedeUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        SedeListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        SedeCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        SedeUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SedeDeleteApiView.as_view(),
        name="delete",
    ),
]
