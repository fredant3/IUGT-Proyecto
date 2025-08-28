from django.urls import path
from emergencia.operaciones.views.create_view import EmergenciaCreateView
from emergencia.operaciones.views.delete_view import EmergenciaDeleteView
from emergencia.operaciones.views.list_view import EmergenciaListView
from emergencia.operaciones.views.update_view import EmergenciaUpdateView
from emergencia.operaciones.views.export_view import EmergenciaExcelView


urlpatterns = [
    path("", EmergenciaListView.as_view(), name="list"),
    path("create", EmergenciaCreateView.as_view(), name="create"),
    path("<int:pk>/read", EmergenciaListView.as_view(), name="read"),
    path("<int:pk>/update", EmergenciaUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", EmergenciaDeleteView.as_view(), name="delete"),
    path("export", EmergenciaExcelView.as_view(), name="export_excel"),
]
