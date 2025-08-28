from django.urls import path
from emergencia.incidencias.views.create_view import IncidenciasCreateApiView
from emergencia.incidencias.views.delete_view import IncidenciasDeleteApiView
from emergencia.incidencias.views.list_view import IncidenciasListApiView
from emergencia.incidencias.views.update_view import IncidenciasUpdateApiView

urlpatterns = [
    path("", IncidenciasListApiView.as_view(), name="list"),
    path("create", IncidenciasCreateApiView.as_view(), name="create"),
    path("<int:pk>/update", IncidenciasUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete", IncidenciasDeleteApiView.as_view(), name="delete"),
]
