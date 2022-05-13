from dataclasses import fields
from django import forms
from .models import Tercero

class TerceroForm(forms.ModelForm):
    class Meta:
        model= Tercero
        fields= '__all__'