from dataclasses import fields
from django import forms
from .models import Dato, Notificacion

class DatoForm(forms.ModelForm):
    class Meta:
        model = Dato
        fields = '__all__'

class NotificacionForm(forms.ModelForm):
    class Meta:
        model=Notificacion
        fields='__all__'