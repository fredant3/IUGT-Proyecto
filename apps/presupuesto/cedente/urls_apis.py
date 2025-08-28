from django.urls import path

from presupuesto.cedente.views.create_view import CedenteCreateApiView
from presupuesto.cedente.views.delete_view import CedenteDeleteApiView
from presupuesto.cedente.views.export_view import CedenteExcelView
from presupuesto.cedente.views.list_view import CedenteListApiView
from presupuesto.cedente.views.update_view import CedenteUpdateApiView

urlpatterns = [
    path(
        "",
        CedenteListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CedenteCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        CedenteUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CedenteDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export",
        CedenteExcelView.as_view(),
        name="export_excel",
    ),
]
