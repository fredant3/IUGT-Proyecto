from django.urls import path

from presupuesto.asignacion.views.create_view import AsignacionCreateView
from presupuesto.asignacion.views.delete_view import AsignacionDeleteView
from presupuesto.asignacion.views.list_view import AsignacionListView
from presupuesto.asignacion.views.update_view import AsignacionUpdateView
from presupuesto.asignacion.views.export_view import AsignacionExcelView

urlpatterns = [
    path(
        "",
        AsignacionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        AsignacionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        AsignacionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        AsignacionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AsignacionDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        AsignacionExcelView.as_view(),
        name="export_excel",
    ),
]
