from django.urls import path
from tecnologia.usuarios.views.delete_view import UserDeleteView
from tecnologia.usuarios.views.list_view import UserListView
from tecnologia.usuarios.views.update_view import UserUpdateView


urlpatterns = [
    path("", UserListView.as_view(), name="list"),
    path("<int:pk>/update", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", UserDeleteView.as_view(), name="delete"),
]
