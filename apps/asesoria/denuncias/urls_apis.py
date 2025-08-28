from asesoria.denuncias.views.create_view import DenunciaCreateApiView
from asesoria.denuncias.views.delete_view import DenunciaDeleteApiView
from asesoria.denuncias.views.export_view import DenunciaExcelView
from asesoria.denuncias.views.list_view import DenunciaListApiView
from asesoria.denuncias.views.update_view import DenunciaUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        DenunciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        DenunciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DenunciaDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        DenunciaExcelView.as_view(),
        name="export_excel",
    ),
]
