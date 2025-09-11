from django import forms


class FormBase(forms.ModelForm):
    container_class = ""
    input_class = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # Verificar si el widget es un Select
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({"class": "input__select"})
            # Verificar si el widget es un Input (TextInput, NumberInput, etc.)
            elif isinstance(
                field.widget, (forms.TextInput, forms.NumberInput, forms.EmailInput)
            ):
                field.widget.attrs.update({"class": "input__input"})
            # Si deseas incluir Textarea
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "input__textarea"})
            # Verificar si el widget es un FileField
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update(
                    {
                        "class": "input__file",
                        "onchange": "displayFileName(this)",
                        "data-text": "Subir archivo",
                    }
                )
            # Verificar si el widget es un CheckboxInput
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "input__checkbox"})

    @staticmethod
    def create_date_field(field_name, title=None):
        return forms.DateField(
            widget=forms.TextInput(attrs={"type": "date"}),
            # input_formats=["%d/%m/%Y"],
            error_messages={"invalid": "Ingrese la fecha en el formato DD/MM/YYYY."},
            # No asignar el label aquí si ya está definido en el Meta del formulario
            label=title if title is not None else None,
        )

    @staticmethod
    def create_time_field(
        field_name,
        title=None,
    ):
        return forms.TimeField(
            widget=forms.TextInput(attrs={"type": "time"}),
            # input_formats=["%H:%M"],
            error_messages={"invalid": "Ingrese la hora en el formato HH:MM."},
            label=title.capitalize() if title is not None else None,
        )
