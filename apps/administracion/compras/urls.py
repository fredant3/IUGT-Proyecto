from administracion.compras.views.create_view import CompraCreateView
from administracion.compras.views.delete_view import CompraDeleteView
from administracion.compras.views.list_view import ComprasListView
from administracion.compras.views.update_view import CompraUpdateView
from administracion.compras.views.export_view import CompraExcelView

from django.urls import path

urlpatterns = [
    path(
        "",
        ComprasListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CompraCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ComprasListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CompraUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CompraDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        CompraExcelView.as_view(),
        name="export_excel",
    ),
]
