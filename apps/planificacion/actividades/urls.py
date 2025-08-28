from django.urls import path
from planificacion.actividades.views.create_view import ActividadCreateView
from planificacion.actividades.views.delete_view import ActividadDeleteView
from planificacion.actividades.views.list_view import ActividadListView
from planificacion.actividades.views.update_view import ActividadUpdateView
from planificacion.actividades.views.export_view import ActividadExcelView

urlpatterns = [
    path(
        "",
        ActividadListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ActividadCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ActividadListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ActividadUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ActividadDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        ActividadExcelView.as_view(),
        name="export",
    ),
]
