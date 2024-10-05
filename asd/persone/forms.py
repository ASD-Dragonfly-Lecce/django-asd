from django import forms
from .models import Persona, Timbratura

class TesseratoForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nome', 'cognome', 'datanascita', 'email1')


class TimbraturaForm(forms.ModelForm):
    class Meta:
        model = Timbratura
        fields = ('categoria', 'note')