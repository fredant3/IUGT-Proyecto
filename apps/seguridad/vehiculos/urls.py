from django.urls import path

from seguridad.vehiculos.views.create_view import VehiculoCreateView
from seguridad.vehiculos.views.delete_view import VehiculoDeleteView
from seguridad.vehiculos.views.list_view import VehiculoListView
from seguridad.vehiculos.views.update_view import VehiculoUpdateView

urlpatterns = [
    path(
        "",
        VehiculoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        VehiculoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        VehiculoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        VehiculoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        VehiculoDeleteView.as_view(),
        name="delete",
    ),
]
