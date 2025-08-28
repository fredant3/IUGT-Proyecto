from django.urls import path
from gestion_comunicacional.frente_preventivo.views.create_view import (
    FrentepreventivoCreateApiView,
)
from gestion_comunicacional.frente_preventivo.views.delete_view import (
    FrentepreventivoDeleteApiView,
)
from gestion_comunicacional.frente_preventivo.views.list_view import (
    FrentepreventivoListApiView,
)
from gestion_comunicacional.frente_preventivo.views.update_view import (
    FrentepreventivoUpdateApiView,
)

urlpatterns = [
    path(
        "",
        FrentepreventivoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        FrentepreventivoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        FrentepreventivoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        FrentepreventivoDeleteApiView.as_view(),
        name="delete",
    ),
]
