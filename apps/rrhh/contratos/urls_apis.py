from django.urls import path

from rrhh.contratos.views.create_view import ContratoCreateApiView
from rrhh.contratos.views.delete_view import ContratoDeleteApiView
from rrhh.contratos.views.list_view import ContratoListApiView
from rrhh.contratos.views.update_view import ContratoUpdateApiView
from rrhh.contratos.views.export_view import ContratoExcelView

urlpatterns = [
    path(
        "",
        ContratoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ContratoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ContratoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ContratoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        ContratoExcelView.as_view(),
        name="export_excel",
    ),
]
