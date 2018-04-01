from django import forms
from .validators import validate_url, validate_dot_com

class URLForm(forms.Form):
    url = forms.CharField(label='',
        validators=[validate_url,],
        widget= forms.TextInput(
                attrs={
                "placeholder": "a very, very long URL",
                "class": "form-control"
                }
                )
        )

