from django.urls import path
from tecnologia.groups.views.create_view import GroupPermisosCreateApiView
from tecnologia.groups.views.delete_view import GroupPermisosDeleteApiView
from tecnologia.groups.views.list_view import GroupPermisosListApiView
from tecnologia.groups.views.update_view import GroupPermisosUpdateApiView

urlpatterns = [
    path("", GroupPermisosListApiView.as_view(), name="list"),
    path("create/", GroupPermisosCreateApiView.as_view(), name="create"),
    path("<int:pk>/update/", GroupPermisosUpdateApiView.as_view(), name="update"),
    path("<int:pk>/delete/", GroupPermisosDeleteApiView.as_view(), name="delete"),
    path("<int:pk>/read", GroupPermisosListApiView.as_view(), name="read"),
]
