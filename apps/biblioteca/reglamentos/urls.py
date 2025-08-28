from django.urls import path

from biblioteca.reglamentos.views.list_view import ReglamentosListView

urlpatterns = [
    path("", ReglamentosListView.as_view(), name="list"),
]
