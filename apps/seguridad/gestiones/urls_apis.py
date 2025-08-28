from django.urls import path

from seguridad.gestiones.views.create_view import GestionCreateApiView
from seguridad.gestiones.views.delete_view import GestionDeleteApiView
from seguridad.gestiones.views.list_view import GestionListApiView
from seguridad.gestiones.views.update_view import GestionUpdateApiView
from seguridad.gestiones.views.export_view import GestionExcelView

urlpatterns = [
    path(
        "",
        GestionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        GestionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        GestionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        GestionDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export",
        GestionExcelView.as_view(),
        name="export_excel"),
]
