from asesoria.filmicos.views.create_view import RegistroFilmicoCreateApiView
from asesoria.filmicos.views.delete_view import RegistroFilmicoDeleteApiView
from asesoria.filmicos.views.export_view import RegistroFilmicoExcelView
from asesoria.filmicos.views.list_view import RegistroFilmicoListApiView
from asesoria.filmicos.views.update_view import RegistroFilmicoUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        RegistroFilmicoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        RegistroFilmicoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        RegistroFilmicoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        RegistroFilmicoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        RegistroFilmicoExcelView.as_view(),
        name="export_excel",
    ),
]
