from django.urls import path

from presupuesto.acciones.views.create_view import AccionCreateView
from presupuesto.acciones.views.delete_view import AccionDeleteView
from presupuesto.acciones.views.list_view import AccionListView
from presupuesto.acciones.views.update_view import AccionUpdateView
from presupuesto.acciones.views.export_view import AccionExcelView

urlpatterns = [
    path(
        "",
        AccionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        AccionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        AccionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        AccionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AccionDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        AccionExcelView.as_view(),
        name="export_excel",
    ),
]
