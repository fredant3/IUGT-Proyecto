from django.urls import path
from tecnologia.views.list_view import TecnologiaListApiView
from tecnologia.views.update_view import TecnologiaUpdateApiView

urlpatterns = [
    path(
        "",
        TecnologiaListApiView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/read",
        TecnologiaListApiView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TecnologiaUpdateApiView.as_view(),
        name="update",
    ),
]
