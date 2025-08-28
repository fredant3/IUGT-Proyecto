# forms.py
from django.forms import TextInput
from django.core.validators import MinLengthValidator
from .models import Organismo
from helpers.FormBase import FormBase

class OrganismoForm(FormBase):
    class Meta:
        model = Organismo
        fields = ["nombre"]
        widgets = {
            "nombre": TextInput(attrs={
                "placeholder": "Ej. Bomberos, Policía, etc.",
                "class": "form-control"
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].validators.append(MinLengthValidator(3))
        