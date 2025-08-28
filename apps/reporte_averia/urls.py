from reporte_averia.views.create_view import Reporte_AveriaCreateView
from reporte_averia.views.delete_view import Reporte_AveriaDeleteView
from reporte_averia.views.list_view import Reporte_AveriaListView
from reporte_averia.views.update_view import Reporte_AveriaUpdateView

from django.urls import path

urlpatterns = [
    path(
        "",
        Reporte_AveriaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        Reporte_AveriaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        Reporte_AveriaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        Reporte_AveriaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        Reporte_AveriaDeleteView.as_view(),
        name="delete",
    ),
]
