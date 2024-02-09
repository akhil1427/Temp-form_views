from django import forms
from app.models import *
class collageform(forms.ModelForm):
    class Meta:
        model=collage
        fields='__all__'