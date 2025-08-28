from django.urls import path

from potencia.incidencias.views.create_view import IncidenciaCreateApiView
from potencia.incidencias.views.delete_view import IncidenciaDeleteApiView
from potencia.incidencias.views.list_view import IncidenciaListApiView
from potencia.incidencias.views.update_view import IncidenciaUpdateApiView

urlpatterns = [
    path(
        "",
        IncidenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        IncidenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        IncidenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        IncidenciaDeleteApiView.as_view(),
        name="delete",
    ),
]
