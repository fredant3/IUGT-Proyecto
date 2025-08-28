from django.urls import path
from gestion_comunicacional.views.create_view import GestioncomunicacionalCreateView
from gestion_comunicacional.views.delete_view import GestioncomunicacionalDeleteView
from gestion_comunicacional.views.list_view import GestioncomunicacionalListView
from gestion_comunicacional.views.update_view import GestioncomunicacionalUpdateView


urlpatterns = [
    path("", GestioncomunicacionalListView.as_view(), name="list"),
    path("create", GestioncomunicacionalCreateView.as_view(), name="create"),
    path("<int:pk>/read", GestioncomunicacionalListView.as_view(), name="read"),
    path("<int:pk>/update", GestioncomunicacionalUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", GestioncomunicacionalDeleteView.as_view(), name="delete"),
]
