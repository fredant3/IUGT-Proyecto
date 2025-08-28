from django.urls import path
from planificacion.infraestructuras.views.create_view import (
    InfraestructuraCreateApiView,
)
from planificacion.infraestructuras.views.delete_view import (
    InfraestructuraDeleteApiView,
)
from planificacion.infraestructuras.views.list_view import InfraestructuraListApiView
from planificacion.infraestructuras.views.update_view import (
    InfraestructuraUpdateApiView,
)

urlpatterns = [
    path(
        "",
        InfraestructuraListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        InfraestructuraCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        InfraestructuraUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        InfraestructuraDeleteApiView.as_view(),
        name="delete",
    ),
]
