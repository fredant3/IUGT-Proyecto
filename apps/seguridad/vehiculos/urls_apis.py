from django.urls import path
from seguridad.vehiculos.views.create_view import VehiculoCreateApiView
from seguridad.vehiculos.views.delete_view import VehiculoDeleteApiView
from seguridad.vehiculos.views.list_view import VehiculoListApiView
from seguridad.vehiculos.views.update_view import VehiculoUpdateApiView
from seguridad.vehiculos.views.export_view import VehiculoExcelView

urlpatterns = [
    path(
        "",
        VehiculoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        VehiculoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        VehiculoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        VehiculoDeleteApiView.as_view(),
        name="delete",
    ),
    path
    ("export",
    VehiculoExcelView.as_view(),
    name="export_excel"),
]
