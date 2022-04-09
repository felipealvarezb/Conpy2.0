from dataclasses import fields
from django import forms
from .models import Dato

class DatoForm(forms.ModelForm):
    class Meta:
        model = Dato
        fields = '__all__'