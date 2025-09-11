from django.urls import path
from tecnologia.auditoria.list_view import AuditoriaListApiView

urlpatterns = [
    path("", AuditoriaListApiView.as_view(), name="list"),
]
