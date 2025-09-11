from administracion.asignaciones.views.create_view import AsignacionCreateApiView
from administracion.asignaciones.views.delete_view import AsignacionDeleteApiView
from administracion.asignaciones.views.list_view import AsignacionListApiView
from administracion.asignaciones.views.update_view import AsignacionUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        AsignacionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        AsignacionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        AsignacionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AsignacionDeleteApiView.as_view(),
        name="delete",
    ),
]
