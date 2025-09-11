from django.urls import path
from tecnologia.groups.views.create_view import GroupPermisosCreateView
from tecnologia.groups.views.delete_view import GroupPermisosDeleteView
from tecnologia.groups.views.list_view import GroupPermisosListView
from tecnologia.groups.views.update_view import GroupPermisosUpdateView

urlpatterns = [
    path("", GroupPermisosListView.as_view(), name="list"),
    path("create/", GroupPermisosCreateView.as_view(), name="create"),
    path("<int:pk>/update/", GroupPermisosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", GroupPermisosDeleteView.as_view(), name="delete"),
    path("<int:pk>/read", GroupPermisosListView.as_view(), name="read"),
]
