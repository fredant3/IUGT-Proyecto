from django.urls import path

from biblioteca.normativas.views.list_view import NormativaListApiView

urlpatterns = [
    path("", NormativaListApiView.as_view(), name="list"),
]
