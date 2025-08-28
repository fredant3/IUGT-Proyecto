from asesoria.filmicos.views.create_view import RegistroFilmicoCreateView
from asesoria.filmicos.views.delete_view import RegistroFilmicoDeleteView
from asesoria.filmicos.views.list_view import RegistroFilmicoListView
from asesoria.filmicos.views.update_view import RegistroFilmicoUpdateView
from django.urls import path

urlpatterns = [
    path("", RegistroFilmicoListView.as_view(), name="list"),
    path("create", RegistroFilmicoCreateView.as_view(), name="create"),
    path("<int:pk>/read", RegistroFilmicoListView.as_view(), name="read"),
    path("<int:pk>/update", RegistroFilmicoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", RegistroFilmicoDeleteView.as_view(), name="delete"),
]
