from django.urls import path

from rrhh.cargos.views.create_view import CargoCreateView
from rrhh.cargos.views.delete_view import CargoDeleteView
from rrhh.cargos.views.list_view import CargoListView
from rrhh.cargos.views.update_view import CargoUpdateView
from rrhh.cargos.views.export_view import CargoExcelView

urlpatterns = [
    path(
        "",
        CargoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CargoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CargoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CargoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CargoDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        CargoExcelView.as_view(),
        name="export_excel",
    ),
]
