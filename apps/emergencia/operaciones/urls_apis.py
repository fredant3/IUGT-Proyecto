from django.urls import path
from emergencia.operaciones.views.create_view import EmergenciaCreateApiView
from emergencia.operaciones.views.delete_view import EmergenciaDeleteApiView
from emergencia.operaciones.views.list_view import EmergenciaListApiView
from emergencia.operaciones.views.update_view import EmergenciaUpdateApiView

urlpatterns = [
    path(
        "",
        EmergenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EmergenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EmergenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EmergenciaDeleteApiView.as_view(),
        name="delete",
    ),
]
