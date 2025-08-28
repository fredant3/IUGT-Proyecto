from django.urls import path

from presupuesto.traspaso.views.delete_view import TraspasoDeleteView
from presupuesto.traspaso.views.update_view import TraspasoUpdateWizardView
from presupuesto.traspaso.views.create_view import TraspasoWizardView
from presupuesto.traspaso.views.list_view import TraspasoListView

urlpatterns = [
    path(
        "",
        TraspasoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TraspasoWizardView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TraspasoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TraspasoUpdateWizardView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TraspasoDeleteView.as_view(),
        name="delete",
    ),
]
