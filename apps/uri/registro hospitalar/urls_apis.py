from django.urls import path

from .views.create_view import IncidenciaCreateApiView
from .views.delete_view import IncidenciaDeleteApiView
from .views.list_view import IncidenciaListApiView
from .views.update_view import IncidenciaUpdateApiView

urlpatterns = [
    path(
        "",
        IncidenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        IncidenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        IncidenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        IncidenciaDeleteApiView.as_view(),
        name="delete",
    ),
]
