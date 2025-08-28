from django.urls import path
from potencia.uri.view.create_view import InfogeneralWizardView
from potencia.uri.view.delete_view import UriDeleteView
from potencia.uri.view.list_view import UriListView
from potencia.uri.view.update_view import UriUpdateWizardView

urlpatterns = [
    path(
        "",
        UriListView.as_view(),
        name="list",
    ),
    path(
        "create",
        InfogeneralWizardView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        UriListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        UriUpdateWizardView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        UriDeleteView.as_view(),
        name="delete",
    ),
]
