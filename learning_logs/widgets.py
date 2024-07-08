
from django.forms.widgets import TextInput


class ColorPickerWidget(TextInput):
    input_type = 'color'
