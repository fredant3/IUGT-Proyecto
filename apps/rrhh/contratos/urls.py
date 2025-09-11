from django.urls import path
from rrhh.contratos.views.create_view import rrhhWizardView
from rrhh.contratos.views.create_view import ContratoCreateView
from rrhh.contratos.views.delete_view import ContratoDeleteView
from rrhh.contratos.views.list_view import ContratoListView
from rrhh.contratos.views.update_view import ContratoUpdateWizardView
from rrhh.contratos.views.export_view import ContratoExcelView

urlpatterns = [
    path(
        "",
        ContratoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        rrhhWizardView.as_view(),
        name="create",
    ),
    path(
        "create",
        ContratoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ContratoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ContratoUpdateWizardView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ContratoDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        ContratoExcelView.as_view(),
        name="export_excel",
    ),
]
