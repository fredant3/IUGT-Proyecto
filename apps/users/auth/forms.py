from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["maxlength"] = "10"
        self.fields["username"].widget.attrs["autocomplete"] = "off"
        self.fields["username"].widget.attrs[
            "placeholder"
        ] = "Ingrese su cédula de identidad"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "************"
