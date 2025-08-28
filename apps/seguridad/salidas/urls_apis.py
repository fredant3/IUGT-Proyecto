from django.urls import path

from seguridad.salidas.views.create_view import SalidaCreateApiView
from seguridad.salidas.views.delete_view import SalidaDeleteApiView
from seguridad.salidas.views.list_view import SalidaListApiView
from seguridad.salidas.views.update_view import SalidaUpdateApiView
from seguridad.salidas.views.export_view import SalidaExcelView

urlpatterns = [
    path(
        "",
        SalidaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        SalidaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        SalidaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SalidaDeleteApiView.as_view(),
        name="delete",
    ),

    path(
        "export",
        SalidaExcelView.as_view(),
        name="export_excel"),
]
