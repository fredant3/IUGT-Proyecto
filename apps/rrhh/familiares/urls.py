from django.urls import path

from rrhh.familiares.views.create_view import FamiliarCreateView
from rrhh.familiares.views.delete_view import FamiliarDeleteView
from rrhh.familiares.views.list_view import FamiliarListView
from rrhh.familiares.views.update_view import FamiliarUpdateView
from rrhh.familiares.views.export_view import FamiliarExcelView

urlpatterns = [
    path(
        "",
        FamiliarListView.as_view(),
        name="list",
    ),
    path(
        "create",
        FamiliarCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        FamiliarListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        FamiliarUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        FamiliarDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        FamiliarExcelView.as_view(),
        name="export_excel",
    ),
]
