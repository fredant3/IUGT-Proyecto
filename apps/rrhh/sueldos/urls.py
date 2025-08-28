from django.urls import path

from .views.create_view import SueldoCreateView
from .views.delete_view import SueldoDeleteView
from .views.list_view import SueldoListView
from .views.update_view import SueldoUpdateView
from .views.export_view import SueldoExcelView

urlpatterns = [
    path(
        "",
        SueldoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        SueldoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        SueldoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        SueldoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SueldoDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        SueldoExcelView.as_view(),
        name="export_excel",
    ),
]
