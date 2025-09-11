from administracion.departamentos.views.create_view import DepartamentoCreateView
from administracion.departamentos.views.delete_view import DepartamentoDeleteView
from administracion.departamentos.views.list_view import DepartamentoListView
from administracion.departamentos.views.update_view import DepartamentoUpdateView
from administracion.departamentos.views.export_view import DepartamentoExcelView
from django.urls import path

urlpatterns = [
    path(
        "",
        DepartamentoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DepartamentoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        DepartamentoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DepartamentoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DepartamentoDeleteView.as_view(),
        name="delete",
    ),
        path(
        "export",
        DepartamentoExcelView.as_view(),
        name="export_excel",
    ),
]
