from django.urls import path

from presupuesto.proyecto.views.create_view import ProyectoCreateView
from presupuesto.proyecto.views.delete_view import ProyectoDeleteView
from presupuesto.proyecto.views.list_view import ProyectoListView
from presupuesto.proyecto.views.update_view import ProyectoUpdateView

urlpatterns = [
    path(
        "",
        ProyectoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ProyectoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ProyectoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ProyectoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ProyectoDeleteView.as_view(),
        name="delete",
    ),
]
