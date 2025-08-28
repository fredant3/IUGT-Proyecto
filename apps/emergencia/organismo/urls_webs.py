from django.urls import path
from emergencia.organismo.views.create_view import OrganismoCreateView
from emergencia.organismo.views.delete_view import OrganismoDeleteView
from emergencia.organismo.views.list_view import OrganismoListView
from emergencia.organismo.views.update_view import OrganismoUpdateView
from emergencia.organismo.views.export_view import OrganismoExcelView

urlpatterns = [
    path("", OrganismoListView.as_view(), name="list"),
    path("create/", OrganismoCreateView.as_view(), name="create"),
    path("<int:pk>/update/", OrganismoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", OrganismoDeleteView.as_view(), name="delete"),
    path("export/", OrganismoExcelView.as_view(), name="export_excel"),
]