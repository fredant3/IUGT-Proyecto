from django.urls import path
from emergencia.incidencias.views.create_view import IncidenciasCreateView
from emergencia.incidencias.views.delete_view import IncidenciasDeleteView
from emergencia.incidencias.views.list_view import IncidenciasListView
from emergencia.incidencias.views.update_view import IncidenciasUpdateView
from emergencia.incidencias.views.export_view import IncidenciasExcelView

urlpatterns = [
    path("", IncidenciasListView.as_view(), name="list"),
    path("create/", IncidenciasCreateView.as_view(), name="create"),
    path("<int:pk>/update/", IncidenciasUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", IncidenciasDeleteView.as_view(), name="delete"),
    path("export/", IncidenciasExcelView.as_view(), name="export_excel"),
]