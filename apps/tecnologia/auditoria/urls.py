from django.urls import path
from tecnologia.auditoria.list_view import AuditoriaListView


urlpatterns = [
    path("", AuditoriaListView.as_view(), name="list"),
]
