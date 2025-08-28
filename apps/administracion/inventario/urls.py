from administracion.inventario.views.create_view import ArticuloCreateView
from administracion.inventario.views.delete_view import ArticuloDeleteView
from administracion.inventario.views.list_view import ArticuloListView
from administracion.inventario.views.update_view import ArticuloUpdateView
from administracion.inventario.views.export_view import ArticuloExcelView
from django.urls import path

urlpatterns = [
    path(
        "",
        ArticuloListView.as_view(),
        name="list",
    ),
    path(
        "create/<str:type>/",
        ArticuloCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ArticuloListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ArticuloUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ArticuloDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        ArticuloExcelView.as_view(),
        name="export_excel",
    ),
]
