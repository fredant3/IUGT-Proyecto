from potencia.tipo_incidencia.views.create_view import TipoIncidenciaCreateApiView
from potencia.tipo_incidencia.views.delete_view import TipoIncidenciaDeleteApiView
from potencia.tipo_incidencia.views.list_view import TipoIncidenciaListApiView
from potencia.tipo_incidencia.views.update_view import TipoIncidenciaUpdateApiView
from potencia.tipo_incidencia.views.export_view import TipoIncidenciaExcelApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        TipoIncidenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoIncidenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoIncidenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoIncidenciaDeleteApiView.as_view(),
        name="delete",
    ),

    path
        ("export",
        TipoIncidenciaExcelApiView.as_view(),
        name="export_excel",),
]
