from django import forms
from .models import Persona

class TesseratoForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nome', 'cognome', 'datanascita', 'email1')