from reporte_averia.views.create_view import Reporte_AveriaCreateApiView
from reporte_averia.views.delete_view import Reporte_AveriaDeleteApiView
from reporte_averia.views.list_view import Reporte_AveriaListApiView
from reporte_averia.views.update_view import Reporte_AveriaUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        Reporte_AveriaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        Reporte_AveriaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        Reporte_AveriaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        Reporte_AveriaDeleteApiView.as_view(),
        name="delete",
    ),
]
