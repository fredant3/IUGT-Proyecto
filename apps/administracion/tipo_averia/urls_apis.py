from administracion.tipo_averia.views.create_view import TipoAveriaCreateApiView
from administracion.tipo_averia.views.delete_view import TipoAveriaDeleteApiView
from administracion.tipo_averia.views.list_view import TipoAveriaListApiView
from administracion.tipo_averia.views.update_view import TipoAveriaUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        TipoAveriaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoAveriaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoAveriaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoAveriaDeleteApiView.as_view(),
        name="delete",
    ),
]
