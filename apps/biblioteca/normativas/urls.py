from django.urls import path

from biblioteca.normativas.views.list_view import NormativaListView

urlpatterns = [
    path("", NormativaListView.as_view(), name="list"),
]
