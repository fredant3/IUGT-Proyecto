from django.urls import path

from biblioteca.reglamentos.views.list_view import ReglamentosListApiView

urlpatterns = [
    path("", ReglamentosListApiView.as_view(), name="list"),
]
