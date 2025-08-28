from administracion.sedes.views.create_view import SedeCreateView
from administracion.sedes.views.delete_view import SedeDeleteView
from administracion.sedes.views.list_view import SedeListView
from administracion.sedes.views.update_view import SedeUpdateView
from administracion.sedes.views.export_view import SedeExcelView
from django.urls import path

urlpatterns = [
    path(
        "",
        SedeListView.as_view(),
        name="list",
    ),
    path(
        "create",
        SedeCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        SedeListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        SedeUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SedeDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        SedeExcelView.as_view(),
        name="export_excel",
    ),
]
