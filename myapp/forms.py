
from django import forms
from .models import RegImage


class ImageForm(forms.ModelForm):
    class Meta:
        model= RegImage
        fields= ["name", "imagefile"]
