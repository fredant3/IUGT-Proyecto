from django.urls import path

from rrhh.tipos_sueldos.views.create_view import TipoSueldoCreateApiView
from rrhh.tipos_sueldos.views.delete_view import TipoSueldoDeleteApiView
from rrhh.tipos_sueldos.views.list_view import TipoSueldoListApiView
from rrhh.tipos_sueldos.views.update_view import TipoSueldoUpdateApiView
from rrhh.tipos_sueldos.views.export_view import TipoSueldoExcelView

urlpatterns = [
    path(
        "",
        TipoSueldoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoSueldoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoSueldoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoSueldoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        TipoSueldoExcelView.as_view(),
        name="export_excel",
    ),
]
