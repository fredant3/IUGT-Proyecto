from django.urls import path
from emergencia.organismo.views.create_view import OrganismoCreateApiView
from emergencia.organismo.views.delete_view import OrganismoDeleteApiView
from emergencia.organismo.views.list_view import OrganismoListApiView
from emergencia.organismo.views.update_view import OrganismoUpdateApiView

urlpatterns = [
    path("", OrganismoListApiView.as_view(), name="list"),
    path("create", OrganismoCreateApiView.as_view(), name="create"),
    path("<int:pk>/update", OrganismoUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete", OrganismoDeleteApiView.as_view(), name="delete"),
]
