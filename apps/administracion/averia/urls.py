from administracion.averia.views.create_view import AveriaCreateView
from administracion.averia.views.delete_view import AveriaDeleteView
from administracion.averia.views.list_view import AveriaListView
from administracion.averia.views.update_view import AveriaUpdateView
from administracion.averia.views.export_view import AveriaExcelView
from django.urls import path

urlpatterns = [
    path(
        "",
        AveriaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        AveriaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        AveriaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        AveriaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AveriaDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        AveriaExcelView.as_view(),
        name="export_excel",
    ),
]
