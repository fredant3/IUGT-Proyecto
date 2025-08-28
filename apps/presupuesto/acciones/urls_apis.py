from django.urls import path

from presupuesto.acciones.views.create_view import AccionCreateApiView
from presupuesto.acciones.views.delete_view import AccionDeleteApiView
from presupuesto.acciones.views.list_view import AccionListApiView
from presupuesto.acciones.views.update_view import AccionUpdateApiView
from presupuesto.acciones.views.export_view import AccionExcelView

urlpatterns = [
    path(
        "",
        AccionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        AccionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        AccionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AccionDeleteApiView.as_view(),
        name="delete",
    ),
]
