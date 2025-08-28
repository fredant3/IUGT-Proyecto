from django.urls import path
from presupuesto.traspaso.views.export_view import TraspasoExcelView
from presupuesto.traspaso.views.create_view import TraspasoCreateApiView
from presupuesto.traspaso.views.delete_view import TraspasoDeleteApiView
from presupuesto.traspaso.views.list_view import TraspasoListApiView
from presupuesto.traspaso.views.update_view import TraspasoUpdateApiView

urlpatterns = [
    path(
        "",
        TraspasoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TraspasoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TraspasoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TraspasoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export",
        TraspasoExcelView.as_view(),
        name="export_excel",
    ),
]
