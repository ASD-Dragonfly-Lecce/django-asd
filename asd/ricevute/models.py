from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from persone.models import Persona
from django.urls import reverse
from datetime import date


class Ricevuta(models.Model):
    numero = models.CharField(max_length=32, blank=True)
    data = models.DateField(null=True)
    testo = models.TextField(blank=True, null=True)
    creato_il = models.DateTimeField(auto_now_add=True)
    modificato_il = models.DateTimeField(auto_now=True)
    persona = models.ForeignKey(Persona,
                               on_delete=models.CASCADE,
                               related_name='ricevute',
                               blank=True,
                               null=True)
    utente = models.ForeignKey(User,
                               null=True,
                               on_delete=models.CASCADE)
    class Meta:
        ordering = ('numero',)
        verbose_name_plural = "ricevute"

    def __str__(self):
        creato_il = self.creato_il.strftime("%d/%m/%Y %H:%M")
        return f"{creato_il} - {self.numero}"
