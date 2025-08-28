from django.urls import path
from organizacion.reglamentos.views.create_view import ReglamentoCreateApiView
from organizacion.reglamentos.views.delete_view import ReglamentoDeleteApiView
from organizacion.reglamentos.views.list_view import ReglamentoListApiView
from organizacion.reglamentos.views.update_view import ReglamentoUpdateApiView

urlpatterns = [
    path(
        "",
        ReglamentoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReglamentoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ReglamentoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReglamentoDeleteApiView.as_view(),
        name="delete",
    ),
]
