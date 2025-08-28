from django.urls import path
from planificacion.objetivos.views.create_view import ObjetivoCreateView
from planificacion.objetivos.views.delete_view import ObjetivoDeleteView
from planificacion.objetivos.views.list_view import ObjetivoListView
from planificacion.objetivos.views.update_view import ObjetivoUpdateView
from planificacion.objetivos.views.export_view import ObjetivoExcelView

urlpatterns = [
    path(
        "",
        ObjetivoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ObjetivoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ObjetivoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ObjetivoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ObjetivoDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export",
        ObjetivoExcelView.as_view(),
        name="export_excel",
    ),
]
