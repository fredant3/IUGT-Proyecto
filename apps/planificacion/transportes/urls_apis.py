from django.urls import path
from planificacion.transportes.views.create_view import TransporteCreateApiView
from planificacion.transportes.views.delete_view import TransporteDeleteApiView
from planificacion.transportes.views.list_view import TransporteListApiView
from planificacion.transportes.views.update_view import TransporteUpdateApiView

urlpatterns = [
    path(
        "",
        TransporteListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TransporteCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TransporteUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TransporteDeleteApiView.as_view(),
        name="delete",
    ),
]
