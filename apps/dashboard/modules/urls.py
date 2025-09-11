from dashboard.modules.views import Modules
from django.urls import path

urlpatterns = [
    path(
        "",
        Modules.as_view(),
        name="index",
    ),
]
