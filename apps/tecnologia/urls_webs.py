from django.urls import path
from tecnologia.views.list_view import TecnologiaListView
from tecnologia.views.update_view import TecnologiaUpdateView

urlpatterns = [
    path(
        "",
        TecnologiaListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/read",
        TecnologiaListView.as_view(),
        name="read",
    ),
    path("<int:pk>/update", TecnologiaUpdateView.as_view(), name="update"),
]
