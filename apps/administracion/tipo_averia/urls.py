from administracion.tipo_averia.views.create_view import TipoAveriaCreateView
from administracion.tipo_averia.views.delete_view import TipoAveriaDeleteView
from administracion.tipo_averia.views.list_view import TipoAveriaListView
from administracion.tipo_averia.views.update_view import TipoAveriaUpdateView
from administracion.tipo_averia.views.export_view import TipoAveriaExcelView
from django.urls import path

urlpatterns = [
    path(
        "",
        TipoAveriaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoAveriaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TipoAveriaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TipoAveriaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoAveriaDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        TipoAveriaExcelView.as_view(),
        name="export_excel",
    ),
]
