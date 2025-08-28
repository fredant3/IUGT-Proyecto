from administracion.asignaciones.views.create_view import AsignacionCreateView
from administracion.asignaciones.views.delete_view import AsignacionDeleteView
from administracion.asignaciones.views.list_view import AsignacionListView
from administracion.asignaciones.views.update_view import AsignacionUpdateView
from administracion.asignaciones.views.export_view import AsignacionExcelView
from django.urls import path

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
