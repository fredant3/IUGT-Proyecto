from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    URLField,
    SET_NULL,
)
from users.auth.models import User


class RequestLog(Model):
    ip_address = CharField(max_length=50)
    device_type = CharField(max_length=50)
    device_name = CharField(max_length=100)
    operating_system = CharField(max_length=100)
    browser = CharField(max_length=100)
    method = CharField(max_length=10)
    url = URLField(max_length=500)
    timestamp = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.method} request from {self.ip_address} at {self.timestamp}"
