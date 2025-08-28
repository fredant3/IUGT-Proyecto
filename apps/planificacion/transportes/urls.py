from django.urls import path
from planificacion.transportes.views.create_view import TransporteCreateView
from planificacion.transportes.views.delete_view import TransporteDeleteView
from planificacion.transportes.views.list_view import TransporteListView
from planificacion.transportes.views.update_view import TransporteUpdateView
from planificacion.transportes.views.export_view import TransporteExcelView

urlpatterns = [
    path(
        "",
        TransporteListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TransporteCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TransporteListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TransporteUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TransporteDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        TransporteExcelView.as_view(),
        name="export_excel",
    ),
]
