from django.urls import path

from presupuesto.asignacion.views.create_view import AsignacionCreateApiView
from presupuesto.asignacion.views.delete_view import AsignacionDeleteApiView
from presupuesto.asignacion.views.list_view import AsignacionListApiView
from presupuesto.asignacion.views.update_view import AsignacionUpdateApiView

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
