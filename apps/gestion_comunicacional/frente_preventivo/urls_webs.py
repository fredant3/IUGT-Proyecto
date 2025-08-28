from django.urls import path
from gestion_comunicacional.frente_preventivo.views.create_view import (
    FrentepreventivoCreateView,
)
from gestion_comunicacional.frente_preventivo.views.delete_view import (
    FrentepreventivoDeleteView,
)
from gestion_comunicacional.frente_preventivo.views.list_view import (
    FrentepreventivoListView,
)
from gestion_comunicacional.frente_preventivo.views.update_view import (
    FrentepreventivoUpdateView,
)


urlpatterns = [
    path("", FrentepreventivoListView.as_view(), name="list"),
    path("create", FrentepreventivoCreateView.as_view(), name="create"),
    path("<int:pk>/read", FrentepreventivoListView.as_view(), name="read"),
    path("<int:pk>/update", FrentepreventivoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", FrentepreventivoDeleteView.as_view(), name="delete"),
]
