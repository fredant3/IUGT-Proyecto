from django.urls import path

from presupuesto.receptor.views.create_view import ReceptorCreateApiView
from presupuesto.receptor.views.delete_view import ReceptorDeleteApiView
from presupuesto.receptor.views.export_view import ReceptorExcelView
from presupuesto.receptor.views.list_view import ReceptorListApiView
from presupuesto.receptor.views.update_view import ReceptorUpdateApiView

urlpatterns = [
    path(
        "",
        ReceptorListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReceptorCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ReceptorUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReceptorDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export",
        ReceptorExcelView.as_view(),
        name="export_excel",
    ),
]
