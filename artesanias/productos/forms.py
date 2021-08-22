from django import forms
from django.db.models import fields
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','telefono','email','mensaje']