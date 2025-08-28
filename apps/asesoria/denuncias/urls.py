from asesoria.denuncias.views.create_view import DenunciaCreateView
from asesoria.denuncias.views.delete_view import DenunciaDeleteView
from asesoria.denuncias.views.list_view import DenunciaListView
from asesoria.denuncias.views.update_view import DenunciaUpdateView
from django.urls import path

urlpatterns = [
    path(
        "",
        DenunciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        DenunciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DenunciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DenunciaDeleteView.as_view(),
        name="delete",
    ),
]
