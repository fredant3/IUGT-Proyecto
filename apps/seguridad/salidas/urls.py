from django.urls import path

from seguridad.salidas.views.create_view import SalidaCreateView
from seguridad.salidas.views.delete_view import SalidaDeleteView
from seguridad.salidas.views.list_view import SalidaListView
from seguridad.salidas.views.update_view import SalidaUpdateView

urlpatterns = [
    path(
        "",
        SalidaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        SalidaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        SalidaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        SalidaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SalidaDeleteView.as_view(),
        name="delete",
    ),
]
