from django import forms
from .validators import validate_url, validate_dot_com

class URLForm(forms.Form):
    url = forms.CharField(max_length=200, label='Submit URL', validators=[validate_url, validate_dot_com])

