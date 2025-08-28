from django.urls import path
from seguridad.entradas.views.create_view import EntradaCreateView
from seguridad.entradas.views.delete_view import EntradaDeleteView
from seguridad.entradas.views.list_view import EntradaListView
from seguridad.entradas.views.update_view import EntradaUpdateView
from seguridad.entradas.views.export_view import EntradaExcelView

urlpatterns = [
    path(
        "",
        EntradaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EntradaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EntradaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EntradaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EntradaDeleteView.as_view(),
        name="delete",
    ),

    path(
        "export",
        EntradaExcelView.as_view(),
        name="export_excel"),
]
